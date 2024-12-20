from openai import OpenAI
import yaml
import json
from encrypt import getKey

url = "https://api.deepseek.com"

def main():
    key = getKey()
    print(key)

    # client = OpenAI(api_key=key, base_url=url)
    # response = client.chat.completions.create(
    #     model="deepseek-chat",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant"},
    #         {"role": "user", "content": "Hello"},
    #     ],
    #     stream=False
    # )
    # print(response.choices[0].message.content)

if __name__ == "__main__":
    main()