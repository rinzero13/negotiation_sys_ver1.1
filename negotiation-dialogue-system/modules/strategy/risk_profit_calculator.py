class RiskCalculator:
    def calculate(self, emotion, personality, intent):
        risk_score = 0.0
        profit_score = 0.0
        
        # 感情
        if emotion == "negative":
            risk_score += 0.7
            profit_score += 0.2
        elif emotion == "positive":
            risk_score += 0.3
            profit_score += 0.8
        else:
            risk_score += 0.5
            profit_score += 0.5
        
        # 性格
        if personality == "cooperative":
            risk_score += 0.4
            profit_score += 0.5
        elif personality == "competitive":
            risk_score += 0.2
            profit_score += 0.7

        # 意図
        if intent == "counter":
            risk_score += 0.5
            profit_score += 0.3
        
        return risk_score, profit_score