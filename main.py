import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_functions import available_functions
from functions.call_function import call_function
from prompts import system_prompt


if len(sys.argv) < 2 or sys.argv[1] == "--verbose":
    print("Must provide a prompt for the agent")
    sys.exit(1)

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = "gemini-2.0-flash-001"
    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    config = types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions])

    generate_content(client, model_name, messages, config)

def generate_content(client: genai.Client, model_name: str, messages: list[types.Content], config: types.GenerateContentConfig):
    for i in range (0, 20):
        verbose = "--verbose" in sys.argv
        response = client.models.generate_content(model=model_name, contents=messages, config=config)

        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.function_calls:
            messages.extend(handle_calls(response, verbose))
        elif verbose:
            prompt = sys.argv[1]
            print_verbose(prompt, response)
            break
        else:
            break

    print_normal(response)

def handle_calls(response: types.GenerateContentResponse, verbose: bool)-> list[types.Content]:
    messages = []
    for call in response.function_calls:
        print(f"Calling function: {call.name}({call.args})")
        result = call_function(call)
        if not result.parts[0].function_response.response:
            raise Exception("No response from function call")
        
        if verbose:
            print(f"-> {result.parts[0].function_response.response}")
        
        messages.append(result)
    return messages

def print_normal(response: types.GenerateContentResponse):
    print(f"LLM RESPONSE: \n{response.text}")
            
def print_verbose(prompt: str, response: types.GenerateContentResponse):
    print(f"User prompt: {prompt}")
    print_normal(response)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
