import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def count_ratio(pas, total):
            pas = float(pas)
            total = float(total)
            return ((pas + 1.0) / (total + 1.0)) - (pas / total)

        k = []
        for i, j in classes:
            heapq.heappush(k, (-count_ratio(i, j), i, j))


        e = int(extraStudents)

        for _ in range(e):
            p, q, t = heapq.heappop(k)
            heapq.heappush(k, (-count_ratio(q + 1, t + 1), q + 1, t + 1))

        s = 0
        while k:
            o, q, r = heapq.heappop(k)
            q = float(q)
            r = float(r)
            s += q / r

        return s / len(classes)