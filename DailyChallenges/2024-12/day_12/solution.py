class Solution(object):
    def pickGifts(self, gifts, k):
        max_heap = gifts[:]
        n = len(max_heap)

        for i in range(n // 2 - 1, -1, -1):
            heapify(max_heap, n, i)

        for _ in range(k):
            max_gift = extract_max(max_heap)
            new_gift = int(max_gift ** 0.5)
            insert(max_heap, new_gift)

        return sum(max_heap)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(arr, key):
    arr.append(key)
    i = len(arr) - 1
    while i > 0 and arr[(i - 1) // 2] < arr[i]:
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i = (i - 1) // 2

def extract_max(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return arr.pop()

    root = arr[0]
    arr[0] = arr.pop()
    heapify(arr, n - 1, 0)
    return root