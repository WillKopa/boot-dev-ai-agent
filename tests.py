from functions.get_files_info import get_files_info

def tests():
    working_directory = "calculator"
    tests = []
    tests.append(get_files_info(working_directory, "."))
    tests.append(get_files_info(working_directory, "pkg"))
    tests.append(get_files_info(working_directory, "/bin"))
    tests.append(get_files_info(working_directory, "../"))

    for i, test, in enumerate(tests):
        print_tests(test, i+1)
        

def print_tests(func, test_number):
    print(f"TEST {test_number}")
    print("=" * 20)
    print(func)
    print("=" * 20)


tests()