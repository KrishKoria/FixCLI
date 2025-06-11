import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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

    print("Testing get_file_content function:")
    print("=" * 50)
    
    print("Test 5: get_file_content('calculator', 'main.py')")
    result5 = get_file_content("calculator", "main.py")
    print(result5)
    print()
    
    print("Test 6: get_file_content('calculator', 'pkg/calculator.py')")
    result6 = get_file_content("calculator", "pkg/calculator.py")
    print(result6)
    print()
    
    print("Test 7: get_file_content('calculator', '/bin/cat')")
    result7 = get_file_content("calculator", "/bin/cat")
    print(result7)
    print()
    
if __name__ == "__main__":
    main()