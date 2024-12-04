from openai import OpenAI

class IntentAnalyzer:
    def __init__(self, api_key):
       self.client = OpenAI(api_key=api_key)

    def analyze_intent(self, text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "以下のテキストの意図をpropose、counter、agree、disagree、offer、accept、reject、quitに分類してください:"},
                      {"role": "user", "content": text}]
        )
        intent = response.choices[0].message.content
        return intent
