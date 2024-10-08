def roman_to_int(s: str) -> int:

    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0

    for i in range(len(s)):
        current = roman_map[s[i]]
        if i + 1 < len(s) and current < roman_map[s[i + 1]]:
            total -= current
        else:
            total += current
    return total

# テストケース
print(roman_to_int("III"))      # 出力: 3
print(roman_to_int("LVIII"))    # 出力: 58
print(roman_to_int("MCMXCIV"))  # 出力: 1994