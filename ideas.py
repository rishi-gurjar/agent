from litellm import completion
from dotenv import load_dotenv
import os
import sys
import json
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

model="gpt-4o"
def openai_call(messages: list):
    response = completion(
        model=model,
        messages=messages,
        stream=False,
        temperature=0.7,
        response_format={"type": "json_object"},
        max_tokens=1000,
    )
    return response

if __name__ == "__main__":
    interests = "gardening, horticulture, mechanism design, robotics, computer vision"
    content_string = f"""
You an idea generator. The user's interests are given, and you must find adjacent ideas to the user's interests. Your goal is to help the user expand their knowledge, and help them find new interests. The user's interests are: {interests}. Output ideas, projects, and research tangents that the user can pursue. 

Return the information in the following JSON format:
{{
"ideas": [
{{
"idea": "Idea 1",
"description": "Description of Idea 1"
}},
{{
"idea": "Idea 2",
"description": "Description of Idea 2"
}},
{{
"idea": "Idea 3",
"description": "Description of Idea 3"
}}
],
"projects": [
{{
"project": "Project 1",
"description": "Description of Project 1"
}},
{{
"project": "Project 2",
"description": "Description of Project 2"
}},
{{
"project": "Project 3",
"description": "Description of Project 3"
}}
],
"research": [
{{
"research": "Research 1",
"description": "Description of Research 1"
}},
{{
"research": "Research 2",
"description": "Description of Research 2"
}},
{{
"research": "Research 3",
"description": "Description of Research 3"
}}
]
}}
"""
    messages = [
        {"role": "system", "content": content_string},
    ]
    response = openai_call(messages)
    content = response.choices[0].message.content
    data = json.loads(content)
    print(data)
    
    for i in range(len(data["ideas"])):
        print(f"Idea: {data['ideas'][i]['idea']}")
        print(f"Description: {data['ideas'][i]['description']}")
        print("\n")
    for i in range(len(data["projects"])):
        print(f"Project: {data['projects'][i]['project']}")
        print(f"Description: {data['projects'][i]['description']}")
        print("\n")
    for i in range(len(data["research"])):
        print(f"Research: {data['research'][i]['research']}")
        print(f"Description: {data['research'][i]['description']}")
        print("\n")