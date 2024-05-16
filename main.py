from litellm import completion
from dotenv import load_dotenv
import os
import sys
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

model="gpt-4o"
def openai_call(messages: list):
    response = completion(
        model=model,
        messages=messages,
        stream=True,
        temperature=0.7,
        #response_format={"type": "json_object"},
        max_tokens=1000,
    )

    accuumulated_text = ""
    for chunk in response:
        words = chunk.choices[0].delta.content or ""
        sys.stdout.write(words)
        sys.stdout.flush()
        accuumulated_text += words


    messages.append(
        {"role": "assistant", "content": accuumulated_text}
    )
    with open('data.txt', 'a') as f:
        f.write(f"AI: {accuumulated_text}\n")
    print("\n")

    return messages

def read_data_file():
    with open('data.txt', 'r') as f:
        data = f.read()
    return data


def runner():
    data_str = read_data_file()
    messages = [
        {"role": "system", "content": f"You are a helpful assistant. Answer any questions the user asks. I have attached your previous conversations with the user here: {data_str}"},
    ]
    while True:
        user_input = input("You: ")
        messages.append(
            {"role": "user", "content": user_input}
        )
        with open('data.txt', 'a') as f:
            f.write(f"User: {user_input}\n")
        messages = openai_call(messages)

if __name__ == "__main__":
    runner()

    # local memory stored in messages
    # full memory stored in data.txt