import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(
            os.path.join(abs_working_dir, file_path)
        )

        # Prevent writing outside the working directory
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return (
                f'Error: Cannot write to "{file_path}" '
                "as it is outside the permitted working directory"
            )

        # Prevent writing to a directory
        if os.path.isdir(abs_file_path):
            return (
                f'Error: Cannot write to "{file_path}" '
                "as it is a directory"
            )

        # Create parent directories if they don't exist
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        # Write file
        with open(abs_file_path, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" '
            f'({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"



schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": (
            "Writes or overwrites a file relative to the working directory."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path to the file relative to the working directory."
                    ),
                },
                "content": {
                    "type": "string",
                    "description": (
                        "The content that should be written to the file."
                    ),
                },
            },
            "required": [
                "file_path",
                "content",
            ],
        },
    },
}