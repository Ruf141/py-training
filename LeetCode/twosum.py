class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# クラスを直接インスタンス化して、関数を呼び出す
param_1 = [2, 7, 11, 15]  # 例の配列
param_2 = 9  # 目標値
ret = Solution().twoSum(param_1, param_2)
print(ret)  # 出力: [0, 1]
