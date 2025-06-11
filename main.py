import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Please set the GEMINI_API_KEY environment variable.")
    sys.exit(1)

client = genai.Client(api_key=api_key)
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

res = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

print(res.text)
if verbose:
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")