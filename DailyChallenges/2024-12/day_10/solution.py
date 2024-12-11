class Solution:
    def maximumLength(self, s):
        n = len(s)
        freq = {}

        for i in range(n):
            char = s[i]
            substring = ""
            for j in range(i, n):
                if s[j] == char:
                    substring += s[j]
                    freq[substring] = freq.get(substring, 0) + 1
                else:
                    break

        max_length = -1
        for substring, count in freq.items():
            if count >= 3:
                max_length = max(max_length, len(substring))

        return max_length