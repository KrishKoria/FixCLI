import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.call_function import call_function
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Please set the GEMINI_API_KEY environment variable.")
    sys.exit(1)

client = genai.Client(api_key=api_key)


SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
if len(sys.argv) > 1:
    verbose = "--verbose" in sys.argv
    
    args = [arg for arg in sys.argv[1:] if arg != "--verbose"]
    
    if not args:
        print("Usage: python main.py <prompt> [--verbose]")
        sys.exit(1)
    
    prompt = " ".join(args)
else:
    print("Usage: python main.py <prompt> [--verbose]")
    sys.exit(1)

if verbose:
    print(f"User prompt: {prompt}")

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns its output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory, creating directories if needed.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
res = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=SYSTEM_PROMPT
    ),
)

max_iterations = 20
for iteration in range(max_iterations):
    if verbose:
        print(f"\n--- Iteration {iteration + 1} ---")
    
    res = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=SYSTEM_PROMPT
        ),
    )
    
    function_called = False
    for candidate in res.candidates:
        messages.append(candidate.content)
        
        if candidate.content.parts:
            for part in candidate.content.parts:
                if hasattr(part, 'function_call') and part.function_call:
                    function_called = True
                    function_call_part = part.function_call
                    function_call_result = call_function(function_call_part, verbose)
                    
                    if not (hasattr(function_call_result, 'parts') and 
                            len(function_call_result.parts) > 0 and
                            hasattr(function_call_result.parts[0], 'function_response') and
                            hasattr(function_call_result.parts[0].function_response, 'response')):
                        raise Exception("Function call did not return expected response structure")
                    
                    messages.append(function_call_result)
                    
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
    
    if not function_called:
        if res.text:
            print(res.text)
        break

if verbose:
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")