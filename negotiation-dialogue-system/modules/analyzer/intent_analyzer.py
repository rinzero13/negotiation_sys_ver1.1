from openai import OpenAI

class IntentAnalyzer:
    def __init__(self, api_key):
       self.client = OpenAI(api_key=api_key)

    def analyze_intent(self, text):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "以下のテキストを意図分析してください。出力は必ず次のいずれかのみとします:propose,counter,agree,disagree,offer,accept,reject,quit。"},
                        {"role": "user", "content": text}]
            )
            intent = response.choices[0].message.content
        except Exception as e:
            intent = "offer"
            print(f"Error analyzing intent: {e}")
            
        return intent
