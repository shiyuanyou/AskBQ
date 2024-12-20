from openai import OpenAI
import yaml

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

client = OpenAI(api_key=config['key'], base_url=config['url'])

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)