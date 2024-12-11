class Solution:
    def maxCount(self, banned, n, maxSum):
        banned_set = set(banned)

        available = [i for i in range(1, n + 1) if i not in banned_set]
        available.sort()

        current_sum = 0
        count = 0

        for num in available:
            if current_sum + num > maxSum:
                break
            current_sum += num
            count += 1

        return count