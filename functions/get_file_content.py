import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        # Absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Absolute normalized file path
        target_file = os.path.normpath(
            os.path.join(working_dir_abs, file_path)
        )

        # Validate that file is inside working directory
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return (
                f'Error: Cannot read "{file_path}" '
                "as it is outside the permitted working directory"
            )

        # Validate file exists and is a regular file
        if not os.path.isfile(target_file):
            return (
                f'Error: File not found or is not a regular file: "{file_path}"'
            )

        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)

            # Check whether the file continues
            if f.read(1):
                content += (
                    f'[...File "{file_path}" '
                    f"truncated at {MAX_CHARS} characters]"
                )

        return content

    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": (
            "Reads the contents of a file relative to the working directory."
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
            },
            "required": ["file_path"],
        },
    },
}