import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt


def main() -> None:
    model = "openrouter/free"
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt> [--verbose]")
        return

    verbose_flag = "--verbose" in sys.argv
    prompt = " ".join(arg for arg in sys.argv[1:] if arg != "--verbose")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    for _ in range(20):
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=available_functions,
            temperature=0,
        )

        if response is None or response.usage is None:
            print("Error: empty response from model")
            return

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print("Final response:")
            print(message.content)
            if verbose_flag:
                print(f"User prompt: {prompt}")
                print(f"Prompt tokens : {response.usage.prompt_tokens}")
                print(f"Completion tokens : {response.usage.completion_tokens}")
            return

        for tool_call in message.tool_calls:
            result_message = call_function(
                tool_call,
                verbose=verbose_flag,
            )

            if not result_message["content"]:
                raise Exception("Empty tool response")

            if verbose_flag:
                print(f"-> {result_message['content']}")

            messages.append(result_message)

    print("Error: Agent reached maximum number of iterations.")
    sys.exit(1)
