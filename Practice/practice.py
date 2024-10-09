def roman_to_int(s):
    roman_map = {
        "I": 1, "V": 5, "X": 10, 
        "L": 50, "C": 100, "D": 500, 
        "M": 1000
    }

    total = 0

    for i in range(len(s)):
        print(s)
        current = roman_map[s[i]]
        print("current", current)
        if i + 1 < len(s) and current < roman_map[s[i + 1]]:
                total -= current
        else:
            total += current

    return total

print(roman_to_int("III"))
print(roman_to_int("L"))