from openai import OpenAI
import yaml
import json

from encrypt import getKey
from errorCode import (
    RequestErrorCode,
    hintRequestErrorCode
)

url = "https://api.deepseek.com"

def getResult(client, messages):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False
        )
    except Exception as e:
        error_code = e.code
        print(f"Error code: {error_code}")
        print(f"Error message: {hintRequestErrorCode[error_code]}")
        print(f"Error creating OpenAI client: {e}")
        return
    return response.choices[0].message.content

def main():
    key = getKey()
    try:
        client = OpenAI(api_key=key, base_url=url)
    except Exception as e:
        print(f"Error creating OpenAI client: {e}")
        return
    
    print(client.models.list())
    
    result = getResult(client, [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"}
    ])
    print(result)

if __name__ == "__main__":
    main()