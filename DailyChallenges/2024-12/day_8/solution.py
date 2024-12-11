class Solution:
    def maxTwoEvents(self, events):

        events.sort(key=lambda x: x[1])


        max_value = [0] * len(events)
        max_value[0] = events[0][2]

        for i in range(1, len(events)):
            max_value[i] = max(max_value[i - 1], events[i][2])

        def binary_search(target):
            left, right = 0, len(events) - 1
            while left <= right:
                mid = (left + right) // 2
                if events[mid][1] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        result = 0
        for i, (start, end, value) in enumerate(events):
            j = binary_search(start)
            if j >= 0:
                result = max(result, value + max_value[j])
            else:
                result = max(result, value)

        return result