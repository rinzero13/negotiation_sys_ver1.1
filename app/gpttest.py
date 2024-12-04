import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_key = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=openai_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "以下のテキストの感情をポジティブ、ネガティブ、中立に分類してください："},
              {"role": "user", "content": "今日はとても良い日だった。"}]
)

emotion = response.choices[0].message.content
print(emotion)