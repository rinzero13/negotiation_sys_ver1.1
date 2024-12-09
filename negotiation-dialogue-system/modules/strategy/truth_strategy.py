from openai import OpenAI

class TruthStrategy:
    def __init__(self, api_key):
       self.client = OpenAI(api_key=api_key)

    def generate(self, history):
        # システムメッセージ
        messages = [{"role": "system", "content": "以下の対話履歴に対する発話で、価格や条件について事実情報を提示し、売り手の譲歩を引き出してください。"}]
        
        for entry in history:
            messages.append({"role": entry['role'], "content": entry['content']})
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        
        truth_response = response.choices[0].message.content
        return truth_response