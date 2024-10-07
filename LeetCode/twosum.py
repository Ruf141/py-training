class Solution:
    def twoSum(self, nums, target):
        # 空の辞書を準備。すでに見た数とそのインデックスを記録していく
        seen = {}
        
        # リストの中の各数とそのインデックスを1つずつ確認
        for i, num in enumerate(nums):
            # 今の数に対する補完数（target - num）を計算
            complement = target - num
            
            # 補完数が辞書にあるかチェック（すでに見た数かどうか）
            if complement in seen:
                # 見つかった場合、補完数のインデックスと今の数のインデックスを返す
                return [seen[complement], i]
            
            # 辞書に現在の数をインデックスとともに記録
            seen[num] = i
        
        # 問題文の制約から、必ず一つの解があるのでこれ以上の処理は不要

# 実際に引数を渡してテストする
if __name__ == "__main__":
    # 入力となる配列とターゲット値
    param_1 = [2, 7, 11, 15]  # 配列の要素
    param_2 = 9  # 目標となる合計値

    # Solutionクラスのインスタンスを生成して、twoSumメソッドを呼び出す
    solution = Solution()
    ret = solution.twoSum(param_1, param_2)

    # 結果を表示（期待する出力は [0, 1]）
    print(ret)  # 出力: [0, 1]
