import os
from mlx_lm import load, generate, convert

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
BASE_DIRECTORY = "/Users/rishigurjar/Documents/GitHub/agent/models"
BNB_DIRECTORY = f"{BASE_DIRECTORY}/bnb"
MLX_DIRECTORY = f"{BASE_DIRECTORY}/mlx"

model_directory = f"{BASE_DIRECTORY}/{MODEL_NAME}"
bnb_model_directory = f"{BNB_DIRECTORY}/{MODEL_NAME}"
mlx_model_directory = f"{MLX_DIRECTORY}/{MODEL_NAME}"

model, tokenizer = load(mlx_model_directory)

def looper():
    history = []

    index = 1
    while True:
        prompt = input(f"Question {index}: ")
        history.append(f"Question {index}: " + prompt)
        prompt = "You are an assistant. Answer the question directly and candidly. The conversation history is attached below. Answer this question: " + prompt + "\n" + str(history)
        response = generate(
            model=model,
            tokenizer=tokenizer,
            prompt=prompt,
            max_tokens=1000,
            verbose=True
            )
        history.append(f"Answer {index}: " + response)
        index += 1
looper()
