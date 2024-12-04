import os  # 環境変数の操作に使用
from dotenv import load_dotenv  # .envファイルから環境変数を読み込むために使用
import openai  # OpenAIのAPIを利用するためにインポート

# .envファイルから環境変数をロード
load_dotenv()

# 環境変数からOpenAIのAPIキーを取得
openai.api_key = os.environ['OPENAI_API_KEY']

class EmotionAnalyzer:
    def __init__(self):
        # APIキーは環境変数から直接設定するので、特にこの中では何も設定しません
        pass

    def analyze_emotion(self, text):
        # GPT-3.5 turboを使って感情分析を行う
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "以下のテキストの感情をポジティブ、ネガティブ、中立に分類してください:"},
                {"role": "user", "content": text}
            ],
            stream=True  # ストリーミングモードを有効にする
        )

        # 受け取ったストリームデータを1つずつ処理
        emotion = ""
        for chunk in response:
            # 応答の一部（内容）がある場合のみ出力
            if chunk['choices'][0]['delta'].get('content') is not None:
                emotion += chunk['choices'][0]['delta']['content']

        return emotion.strip()  # 最後に感情を返す

if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    text = "I am so happy today, everything is going well!"
    emotion = analyzer.analyze_emotion(text)
    print(f"Text Emotion: {emotion}")
