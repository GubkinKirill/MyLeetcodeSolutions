class Solution:
    def minimumSize(self, nums, maxOperations):
        def canAchievePenalty(P):
            operations = 0
            for num in nums:
                operations += (num - 1) // P
                if operations > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canAchievePenalty(mid):
                right = mid
            else:
                left = mid + 1

        return left

