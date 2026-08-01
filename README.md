# AI Coding Agent

An LLM-powered coding agent for inspecting files, reading source code, writing changes, and executing Python scripts through tool calling.

This project is structured as a small command-line assistant that can:

- list files and directories
- read file contents
- write or overwrite files
- execute Python files with optional arguments

It is designed as a tool-calling exercise where the model decides which function to use based on the user's request.

## Features

- Four LLM-callable tools with JSON schemas
- Safe path handling inside a configured working directory
- Support for recursive agent loops with multiple tool calls
- Verbose mode for inspecting tool calls and tool outputs
- File read and write operations scoped to the `calculator` workspace

## Project structure

```text
AI_ Codeing_Agent/
├── main.py
├── call_function.py
├── config.py
├── prompts.py
├── src/
│   └── ai_codeing_agent/
│       ├── __init__.py
│       └── cli.py
├── functions/
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
└── calculator/
    ├── main.py
    ├── tests.py
    └── pkg/
        ├── calculator.py
        └── render.py
```

## Requirements

- Python 3.11 or newer
- [`uv`](https://docs.astral.sh/uv/) for running the project
- An `OPENROUTER_API_KEY` set in your environment

## Installation

If dependencies are not installed yet:

```bash
uv sync
```

## Environment variables

Create a `.env` file in the project root or export the variable in your shell:

```env
OPENROUTER_API_KEY=your_api_key_here
```

## Running the agent

Run the CLI with a prompt:

```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20."
```

Verbose mode shows the tool calls and their outputs:

```bash
uv run main.py "read the contents of main.py" --verbose
```

## Available tools

The agent can call four functions:

### `get_files_info`

List files and directories inside a relative directory.

Example:

```text
list the contents of the pkg directory
```

### `get_file_content`

Read the contents of a file.

Example:

```text
read the contents of main.py
```

### `write_file`

Write new content to a file or overwrite an existing one.

Example:

```text
write 'hello' to main.txt
```

### `run_python_file`

Execute a Python file with optional command-line arguments.

Example:

```text
run main.py
```

## How it works

1. The user sends a prompt.
2. The LLM decides which tool to call.
3. The selected tool is executed in the `calculator` working directory.
4. The result is returned to the model.
5. The loop continues until the model gives a final response or the iteration limit is reached.

## Notes

- Paths are resolved relative to the `calculator` directory.
- Tool results are returned as strings.
- The agent currently supports multi-step tool calling, but it does not yet automatically verify fixes unless the model chooses to do so.

## Example prompts

Try prompts like these:

```text
list the contents of the pkg directory
read the contents of main.py
write 'hello' to main.txt
run tests.py
```

## Development

Useful commands:

```bash
uv run main.py "list the contents of the pkg directory"
uv run main.py "read the contents of main.py" --verbose
uv run main.py "run tests.py"
```

If you want to validate the calculator app directly:

```bash
python calculator/tests.py
```

## License

No license has been specified yet.
