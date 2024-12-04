from openai import OpenAI

class EmotionAnalyzer:
    def __init__(self, api_key):
       self.client = OpenAI(api_key=api_key)

    def analyze_emotion(self, text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "以下のテキストの感情をpositive、negative、neutralに分類してください:"},
                      {"role": "user", "content": text}]
        )
        emotion = response.choices[0].message.content
        return emotion
