class Solution(object):
    def isArraySpecial(self, nums, queries):
        n = len(nums)
        is_special = [0] * (n - 1)

        for i in range(n - 1):
            if nums[i] % 2 != nums[i + 1] % 2:
                is_special[i] = 1

        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + is_special[i - 1]

        result = []
        for query in queries:
            left, right = query
            if prefix[right] - prefix[left] == (right - left):
                result.append(True)
            else:
                result.append(False)
        return result