import os
from dotenv import load_dotenv
from modules.dialogue_manager import DialogueManager
from logs.log_config import setup_logging

load_dotenv()

openai_key = os.environ['OPENAI_API_KEY']

setup_logging()

def main():
    dialogue_manager = DialogueManager(openai_key)
    print("交渉を開始してください。(acceptもしくはrejectで対話が終了します。)")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ['accept', 'reject', 'exit']:
            print("対話を終了します。")
            break
        
        system_response = dialogue_manager.generate_response(user_input)
        print(f"System: {system_response}")

if __name__ == "__main__":
    main()
