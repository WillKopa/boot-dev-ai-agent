from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

working_directory = "calculator"

def tests():
    tests = []

    # tests.extend(test_get_files_info())
    # tests.extend(test_get_file_content())
    # tests.extend(test_write_file())
    tests.extend(test_run_python_file())

    for i, test, in enumerate(tests):
        print_tests(test, i+1)
        

def print_tests(func, test_number):
    print(f"TEST {test_number}")
    print("=" * 20)
    print(func)
    print("=" * 20)


def test_get_files_info():
    tests=[]
    tests.append(get_files_info(working_directory, "."))
    tests.append(get_files_info(working_directory, "pkg"))
    tests.append(get_files_info(working_directory, "/bin"))
    tests.append(get_files_info(working_directory, "../"))
    return tests

def test_get_file_content():
    tests=[]
    tests.append(get_file_content(working_directory, "main.py"))
    tests.append(get_file_content(working_directory, "pkg/calculator.py"))
    tests.append(get_file_content(working_directory, "/bin/cat"))
    tests.append(get_file_content(working_directory, "lorem.txt"))
    return tests

def test_write_file():
    tests=[]
    tests.append(write_file(working_directory, "lorem_short.txt", "wait, this isn't lorem ipsum"))
    tests.append(write_file(working_directory, "pkg/morelorem.txt", "lorem upsum dolor sit amet"))
    tests.append(write_file(working_directory, "/tmp/temp.txt", "this should not be allowed"))
    return tests

def test_run_python_file():
    tests=[]
    tests.append(run_python_file(working_directory, "main.py"))
    tests.append(run_python_file(working_directory, "tests.py"))
    tests.append(run_python_file(working_directory, "../main.py"))
    tests.append(run_python_file(working_directory, "nonexistent.py"))
    return tests

tests()