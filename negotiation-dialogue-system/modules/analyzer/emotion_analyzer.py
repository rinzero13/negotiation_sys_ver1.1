from openai import OpenAI

class EmotionAnalyzer:
    def __init__(self, api_key):
       self.client = OpenAI(api_key=api_key)

    def analyze_emotion(self, text):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "以下のテキストを感情分析してください。出力は必ず次のいずれかのみとします: positive, negative, neutral。"},
                          {"role": "user", "content": text}]
            )
            emotion = response.choices[0].message.content
        except Exception as e:
            emotion = "neutral"
            print(f"Error analyzing emotion: {e}")
         
        return emotion
