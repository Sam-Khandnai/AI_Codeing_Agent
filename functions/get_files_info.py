import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # Absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Absolute, normalized path of the requested directory
        target_dir = os.path.normpath(
            os.path.join(working_dir_abs, directory)
        )

        # Ensure target directory is inside working directory
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir])
            == working_dir_abs
        )

        if not valid_target_dir:
            return (
                f'Error: Cannot list "{directory}" '
                "as it is outside the permitted working directory"
            )

        # Ensure target exists and is a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        entries = []
        for name in sorted(os.listdir(target_dir)):
            full_path = os.path.join(target_dir, name)
            kind = "dir" if os.path.isdir(full_path) else "file"
            size = os.path.getsize(full_path) if os.path.isfile(full_path) else 0
            entries.append(f"{name}\t{kind}\t{size} bytes")

        if not entries:
            return f'Success: "{directory}" is empty'

        return "\n".join(entries)

    except Exception as e:
        return f"Error: {e}"



schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": (
            "Lists files in a specified directory relative to the "
            "working directory, providing file size and directory status"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": (
                        "Directory path to list files from, relative "
                        "to the working directory "
                        "(default is the working directory itself)"
                    ),
                },
            },
        },
    },
}
