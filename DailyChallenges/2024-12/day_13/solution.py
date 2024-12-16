class Solution:
    def findScore(self, nums):
        n = len(nums)
        marked = [False] * n
        score = 0


        indexed_nums = sorted((num, i) for i, num in enumerate(nums))

        for value, index in indexed_nums:
            if not marked[index]:
                score += value
                marked[index] = True

                if index > 0:
                    marked[index - 1] = True
                if index < n - 1:
                    marked[index + 1] = True

        return score