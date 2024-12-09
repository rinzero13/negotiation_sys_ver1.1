class DialoguePhase:
    def __init__(self, max_turns=10, max_price_decrease=30):
        self.current_phase = "initial"  # 初期段階
        self.turns = 0
        self.max_turns = max_turns
        self.max_price_decrease = max_price_decrease

    def advance_phase(self):
        #ターン数に基づいて、交渉の段階を進める
        if self.current_phase == "initial":
            if self.turns >= 1:
                self.current_phase = "negotiating"
        elif self.current_phase == "negotiating":
            if self.turns >= self.max_turns:
                self.current_phase = "finalizing"
        elif self.current_phase == "finalizing":
            if self.turns >= self.max_turns:
                self.current_phase = "agreement"  # 合意段階に移行

    def get_phase(self):
        #現在の交渉段階を返す
        return self.current_phase

    def update_turns(self):
        #ターン数と値下げ幅を更新
        self.turns += 1

    def check_for_agreement(self):
        #合意が成立したかを判定
        return self.current_phase == "agreement"
