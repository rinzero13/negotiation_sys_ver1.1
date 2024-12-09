import logging
from modules.analyzer.emotion_analyzer import EmotionAnalyzer
from modules.analyzer.personality_analyzer import PersonalityAnalyzer
from modules.analyzer.intent_analyzer import IntentAnalyzer
from modules.strategy.risk_profit_calculator import RiskCalculator
from modules.strategy.lie_strategy import LieStrategy
from modules.strategy.truth_strategy import TruthStrategy
from modules.price_analyzer import PriceExtractor
from modules.dialogue_phase import DialoguePhase

# log設定
dialogue_log = logging.getLogger('dialogue_log')
emotion_log = logging.getLogger('emotion_log')
personality_log = logging.getLogger('personality_log')
intent_log = logging.getLogger('intent_log')
risk_profit_log = logging.getLogger('risk_profit_log')
price_log = logging.getLogger('price_log')
phase_log = logging.getLogger('phase_log')

class DialogueManager:
    def __init__(self, api_key):
        self.emotion_analyzer = EmotionAnalyzer(api_key)
        self.personality_analyzer = PersonalityAnalyzer(api_key)
        self.intent_analyzer = IntentAnalyzer(api_key)
        self.risk_profit_calculator = RiskCalculator()
        self.lie_strategy = LieStrategy(api_key)
        self.truth_strategy = TruthStrategy(api_key)
        self.price_extractor = PriceExtractor()
        self.previous_price = None  # 前回提示した価格を記録
        self.dialogue_phase = DialoguePhase()
        
        self.history = []
        self.initial_price = None # 初期価格を保存するインスタンス変数
        
    def add_to_history(self, role, content):
        #対話履歴に発話を追加する
        self.history.append({"role": role, "content": content})
        

    def generate_response(self, user_input):
        dialogue_log.info(f"user: {user_input}")
        self.add_to_history("user",user_input)
        
        #対話段階を確認
        dialogue_phase = self.dialogue_phase.get_phase()
        phase_log.info(f"phase:{dialogue_phase}")
        
        #価格情報抽出
        prices_txt = self.price_extractor.extract_price(user_input)
        price_log.info(f"{prices_txt}")
        
        if prices_txt is not None:
            prices = self.price_extractor.parse_price(prices_txt)
            #初期価格設定
            if dialogue_phase == "initial":
                if self.initial_price is None:  # 初期価格がまだ設定されていない場合のみ設定
                    self.initial_price = prices
                    
            if self.initial_price is not None:  # 初期価格が設定されていることを確認
                price_decrease = self.initial_price - prices
                print(price_decrease)
        
        #感情、性格、意図分析
        emotion = self.emotion_analyzer.analyze_emotion(user_input)
        personality = self.personality_analyzer.analyze_personality(user_input)
        intent = self.intent_analyzer.analyze_intent(user_input)
        emotion_log.info(f"Emotion: {emotion}")
        personality_log.info(f"Personality: {personality}")
        intent_log.info(f"Intent: {intent}")
        
        #リスク利益計算
        risk, profit = self.risk_profit_calculator.calculate(emotion, personality, intent)
        risk_profit_log.info(f"Risk: {risk}, Profit: {profit}")

        #嘘/正直戦略判定
        if profit < risk:
            response = self.truth_strategy.generate(self.history)
            dialogue_log.info(f"system(truth): {response}")
        else:
            response = self.lie_strategy.generate(self.history) 
            dialogue_log.info(f"system(lie): {response}")

        self.add_to_history("system", response)
        prices_txt = self.price_extractor.extract_price(response)
        price_log.info(f"{prices_txt}")
        
        #対話段階を更新
        self.dialogue_phase.update_turns()
        self.dialogue_phase.advance_phase()
        
        #確認
        print(self.history)
        #print(self.initial_price)
        
        return response