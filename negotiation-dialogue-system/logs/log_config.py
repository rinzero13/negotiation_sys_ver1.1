import logging

def setup_logging():
    # ログの設定
    logging.basicConfig(
        level=logging.INFO,  # INFOレベル以上のログを記録
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            #logging.FileHandler("negotiation-dialogue-system/logs/http_logs.txt", mode='w'),  # HTTPリクエストログ
            #logging.FileHandler("negotiation-dialogue-system/logs/error_logs.txt", mode='w'),  # エラーログ（上書き）
            #logging.StreamHandler()  # コンソールにも出力
        ]
    )

    # 対話ログ
    dialogue_log = logging.getLogger('dialogue_log')
    dialogue_log.setLevel(logging.INFO)
    dialogue_log.addHandler(logging.FileHandler("negotiation-dialogue-system/logs/dialogue_logs.txt", mode='w'))
    
    # 感情ログ
    emotion_log = logging.getLogger('emotion_log')
    emotion_log.setLevel(logging.INFO)
    emotion_log.addHandler(logging.FileHandler("negotiation-dialogue-system/logs/emotion_logs.txt", mode='w'))
    
    # 性格ログ
    personality_log = logging.getLogger('personality_log')
    personality_log.setLevel(logging.INFO)
    personality_log.addHandler(logging.FileHandler("negotiation-dialogue-system/logs/personality_logs.txt", mode='w'))
    
    # 意図ログ
    intent_log = logging.getLogger('intent_log')
    intent_log.setLevel(logging.INFO)
    intent_log.addHandler(logging.FileHandler("negotiation-dialogue-system/logs/intent_logs.txt", mode='w'))
    
    # リスクリターン値ログ
    risk_profit_log = logging.getLogger('risk_profit_log')
    risk_profit_log.setLevel(logging.INFO)
    risk_profit_log.addHandler(logging.FileHandler("negotiation-dialogue-system/logs/risk_profit_logs.txt", mode='w'))
    
    # 価格ログ
    price_log = logging.getLogger('price_log')
    price_log.setLevel(logging.INFO)
    price_log.addHandler(logging.FileHandler("negotiation-dialogue-system/logs/price_logs.txt", mode='w'))
    
    # 対話段階ログ
    phase_log = logging.getLogger('phase_log')
    phase_log.setLevel(logging.INFO)
    phase_log.addHandler(logging.FileHandler("negotiation-dialogue-system/logs/phase_logs.txt", mode='w'))