def roman_to_int(s):
    # ローマ数字とその値を対応付ける辞書を定義
    roman_map = {
        "I": 1, "V": 5, "X": 10, 
        "L": 50, "C": 100, "D": 500, 
        "M": 1000
    }

    # 合計値を保持する変数
    total = 0

    # ローマ数字を順に処理するループ
    for i in range(len(s)):
        # 現在のローマ数字の値を取得
        current = roman_map[s[i]]
        
        # 次の文字が存在し、かつ現在の値より大きい場合、減算が必要
        # 例: "IV"や"IX"のようなケース
        if i + 1 < len(s) and current < roman_map[s[i + 1]]:
            # 減算して合計に反映
            total -= current
        else:
            # 通常の場合、加算して合計に反映
            total += current
            
    return total

# テストケース
print(roman_to_int("III"))      # 出力: 3
print(roman_to_int("LVIII"))    # 出力: 58
print(roman_to_int("MCMXCIV"))  # 出力: 1994
