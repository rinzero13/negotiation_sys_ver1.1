from openai import OpenAI

class LieStrategy:
    def __init__(self, api_key):
       self.client = OpenAI(api_key=api_key)

    def generate(self, history):
        # システムメッセージ
        messages = [{"role": "system", "content": "以下の対話履歴に対する発話では、価格や条件について事実でない情報を提示し、売り手の譲歩を引き出してください。ただし、矛盾や交渉全体を壊すリスクを避けてください。"}]
        
        for entry in history:
            messages.append({"role": entry['role'], "content": entry['content']})
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        lie_response = response.choices[0].message.content
        return lie_response