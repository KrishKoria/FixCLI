import sys
import os

# Add the functions directory to the path so we can import get_files_info
sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))

from functions.get_files_info import get_files_info

def main():
    print("Testing get_files_info function:")
    print("=" * 50)
    
    # Test 1: Get files info for current directory
    print("Test 1: get_files_info('calculator', '.')")
    result1 = get_files_info("calculator", ".")
    print(result1)
    print()
    
    # Test 2: Get files info for pkg subdirectory
    print("Test 2: get_files_info('calculator', 'pkg')")
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    print()
    
    # Test 3: Try to access /bin (should return error)
    print("Test 3: get_files_info('calculator', '/bin')")
    result3 = get_files_info("calculator", "/bin")
    print(result3)
    print()
    
    # Test 4: Try to access parent directory (should return error)
    print("Test 4: get_files_info('calculator', '../')")
    result4 = get_files_info("calculator", "../")
    print(result4)
    print()

if __name__ == "__main__":
    main()