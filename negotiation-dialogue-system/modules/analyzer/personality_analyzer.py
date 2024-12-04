from openai import OpenAI

class PersonalityAnalyzer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        
    def analyze_personality(self, text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "以下のテキスト発話者の性格をcooperative、competitiveに分類してください:"},
                      {"role": "user", "content": text}]
        )
        personality = response.choices[0].message.content
        return personality
