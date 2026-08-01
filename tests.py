from functions.get_files_info import get_files_info 
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def main():
    working_dir = "calculator"

    print("Testing get_file_content")

    print("===== Test 1 =====")
    root_contans = get_file_content(working_dir, ".")
    print(root_contans)

    print("===== Test 2 =====")
    pkg_contans = get_files_info(working_dir, "pkg")
    print(pkg_contans)

    print("===== Test 3 =====")
    bin_contans = get_files_info(working_dir, "/bin")
    print(bin_contans)

    print("===== Test 4 =====")
    backdir_contans = get_files_info(working_dir, "../")
    print(backdir_contans)

    # #------------------------------------------------------------
    print("Testing get_file_content")

    print("===== Test 1 =====")
    print(get_file_content(working_dir, "lorem.txt"))

    print("===== Test 2 =====")
    print(get_file_content(working_dir, "main.py"))

    print("===== Test 3 =====")
    print(get_file_content(working_dir, "pkg/calculator.py"))

    print("===== Test 4 =====")
    print(get_file_content(working_dir, "/bin/cat"))

    #---------------------------------------------------------------
    print("Testing write_file")

    print("===== Test 1 =====")
    print(write_file(
        working_dir,
        "lorem.txt",
        "wait, this isn't lorem ipsum"
    ))
    print()

    print("===== Test 2 =====")
    print(write_file(
        working_dir,
        "pkg/morelorem.txt",
        "lorem ipsum dolor sit amet"
    ))
    print()

    print("===== Test 3 =====")
    print(write_file(
        working_dir,
        "/tmp/temp.txt",
        "this should not be allowed"
    ))

    #---------------------------------------------------------------

    print("Testing run_python_file")

    print("===== Test 1 =====")
    print(run_python_file(working_dir, "main.py"))
    print()

    print("===== Test 2 =====")
    print(run_python_file(working_dir, "main.py", ["3 + 5"]))
    print()

    print("===== Test 3 =====")
    print(run_python_file(working_dir, "tests.py"))
    print()

    print("===== Test 4 =====")
    print(run_python_file(working_dir, "../main.py"))
    print()

    print("===== Test 5 =====")
    print(run_python_file(working_dir, "nonexistent.py"))
    print()

    print("===== Test 6 =====")
    print(run_python_file(working_dir, "lorem.txt"))
 
main()