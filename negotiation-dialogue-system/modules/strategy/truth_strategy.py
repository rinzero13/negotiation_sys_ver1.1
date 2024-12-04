from openai import OpenAI

class TruthStrategy:
    def __init__(self, api_key):
       self.client = OpenAI(api_key=api_key)

    def generate(self, text, history):
        # システムメッセージ
        messages = [{"role": "system", "content": "あなたは買い手です。交渉においてリスクを減少させつつ、価格をできる限り安くすることを目指します。以下のの対話履歴に基づいて、リスクを避けるために嘘を含まない発話を返答してください:"}]
        
        for entry in history:
            messages.append({"role": entry['role'], "content": entry['content']})
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        
        truth_response = response.choices[0].message.content
        return truth_response