import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

if len(sys.argv) < 2 or sys.argv[1] == "--verbose":
    print("Must provide a prompt for the agent")
    sys.exit(1)

def main():
    load_dotenv()
    verbose = "--verbose" in sys.argv
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    if verbose:
        print_verbose(prompt, response)
    else:
        print_normal(response)


def print_normal(response):
    print(response.text)


def print_verbose(prompt, response):
    print(f"User prompt: {prompt}")
    print_normal(response)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
