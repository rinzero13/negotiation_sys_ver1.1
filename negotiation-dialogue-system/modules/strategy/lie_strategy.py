from openai import OpenAI

class LieStrategy:
    def __init__(self, api_key):
       self.client = OpenAI(api_key=api_key)

    def generate(self, history):
        # システムメッセージ
        messages = [{"role": "system", "content": "あなたは買い手です。交渉においてリスクを減少させつつ、価格をできる限り安くすることを目指します。以下の対話履歴に基づいて、利益を得るために嘘を含めた発話を返答してください:"}]
        
        for entry in history:
            messages.append({"role": entry['role'], "content": entry['content']})
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        lie_response = response.choices[0].message.content
        return lie_response