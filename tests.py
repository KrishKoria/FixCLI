import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))

from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python import run_python_file

def main():
    print("Testing get_files_info function:")
    print("=" * 50)
    
    print("Test 1: get_files_info('calculator', '.')")
    result1 = get_files_info("calculator", ".")
    print(result1)
    print()
    
    print("Test 2: get_files_info('calculator', 'pkg')")
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    print()
    
    print("Test 3: get_files_info('calculator', '/bin')")
    result3 = get_files_info("calculator", "/bin")
    print(result3)
    print()
    
    print("Test 4: get_files_info('calculator', '../')")
    result4 = get_files_info("calculator", "../")
    print(result4)
    print()
    print("Testing write_file function:")
    print("=" * 50)
    
    print('Test 1: write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result1)
    print()
    
    print('Test 2: write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)
    print()
    
    print('Test 3: write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result3)
    print()

    print("Testing run_python_file function:")
    print("=" * 50)
    
    print('Test 1: run_python_file("calculator", "main.py")')
    result1 = run_python_file("calculator", "main.py")
    print(result1)
    print()
    
    print('Test 2: run_python_file("calculator", "tests.py")')
    result2 = run_python_file("calculator", "tests.py")
    print(result2)
    print()
    
    print('Test 3: run_python_file("calculator", "../main.py")')
    result3 = run_python_file("calculator", "../main.py")
    print(result3)
    print()
    
    print('Test 4: run_python_file("calculator", "nonexistent.py")')
    result4 = run_python_file("calculator", "nonexistent.py")
    print(result4)
    print()

    
    
if __name__ == "__main__":
    main()