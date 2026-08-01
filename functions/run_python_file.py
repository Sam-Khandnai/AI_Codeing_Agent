import os
import subprocess
import sys


def run_python_file(
    working_directory: str,
    file_path: str,
    args: list[str] | None = None,
) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(
            os.path.join(abs_working_dir, file_path)
        )

        # Check that the file is inside the working directory
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return (
                f'Error: Cannot execute "{file_path}" '
                "as it is outside the permitted working directory"
            )

        # Check that it exists and is a regular file
        if not os.path.isfile(abs_file_path):
            return (
                f'Error: "{file_path}" does not exist '
                "or is not a regular file"
            )

        # Check extension
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Build command
        command = [sys.executable, abs_file_path]

        if args:
            command.extend(args)

        # Run the process
        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = ""

        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"

        if not result.stdout and not result.stderr:
            output += "No output produced"
        else:
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}"

            if result.stderr:
                output += f"STDERR:\n{result.stderr}"

        return output.rstrip()

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": (
            "Executes a Python file relative to the working directory "
            "with optional command-line arguments."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path to the Python file relative to the working directory."
                    ),
                },
                "args": {
                    "type": "array",
                    "description": (
                        "Optional command-line arguments."
                    ),
                    "items": {
                        "type": "string",
                    },
                },
            },
            "required": ["file_path"],
        },
    },
}
