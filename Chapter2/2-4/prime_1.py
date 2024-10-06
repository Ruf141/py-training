for i in range(2, 101):
    h = i // 2
    f = True
    for j in range(2, h + 1):
        if i % j == 0:
            f = False
            break
    if f == True:
        print(i, end=",")

# 説明変数化したロジック
for number in range(2, 101):
    # 2から100までの整数numberを順に処理
    half_value = number // 2
    # numberの半分の値をhalf_valueに代入（整数の除算）
    is_prime = True

    # 素数判定用のフラグ is_prime をTrueで初期化
    for divisor in range(2, half_value + 1):
        # 2からhalf_valueまでの整数divisorで割り切れるか確認
        if number % divisor == 0:
            # numberがdivisorで割り切れた場合
            is_prime = False
            # is_primeをFalseに設定し、素数ではないと判定
            break
            # 内側のループを抜ける
    if is_prime:
        # is_primeがTrueのままであれば素数
        print(number, end=",")  # 素数を出力


# 一つの数値を素数判定する単純なロジック
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 使用例
num = 29
if is_prime(num):
    print(f"{num}は素数です")
else:
    print(f"{num}は素数ではありません")
