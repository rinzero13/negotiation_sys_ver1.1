from modules.analyzer.emotion_analyzer import EmotionAnalyzer
from config import OPENAI_API_KEY

def main():
    emotion_analyzer = EmotionAnalyzer(api_key=OPENAI_API_KEY)
    print("交渉システムへようこそ！")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ['quit', 'exit']:
            print("対話を終了します。")
            break

        emotion = emotion_analyzer.analyze_emotion(user_input)
        print(f"System: {emotion}")

if __name__ == "__main__":
    main()
