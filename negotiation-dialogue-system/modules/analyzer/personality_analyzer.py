from openai import OpenAI

class PersonalityAnalyzer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        
    def analyze_personality(self, text):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "以下のテキスト発話者の性格分析をしてください。出力は必ず次のいずれかのみとします:cooperative,competitive。"},
                          {"role": "user", "content": text}]
            )
            personality = response.choices[0].message.content
        except Exception as e:
            personality = "cooperative"
            print(f"Error analyzing personality: {e}")

        
        return personality
