import re

class PriceExtractor:
    def extract_price(self, text):
        # 価格を抽出する正規表現（～円）
        price_patterns = [
            r"\d+(?:,\d{3})*(?:\.\d+)?円",    
        ]
        
        for pattern in price_patterns:
            found_prices = re.findall(pattern, text)
            if found_prices:
                return found_prices[0]  # 最初に見つかった価格を返す
        
        return None  # 価格が見つからない場合
    
    def parse_price(self, price_text):
            #抽出された価格テキストを数値型に変換。

            price = re.sub(r'[^\d.]', '', price_text)  # 通貨記号を除去
            try:
                return float(price)
            except ValueError:
                return None

        
