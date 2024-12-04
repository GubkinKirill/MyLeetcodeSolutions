class Solution(object):
    def checkIfExist(self, arr):
        hash_table = set()
        for i in arr:
            if i * 2 in hash_table or (i % 2 == 0 and i //2 in hash_table):
                return True
            hash_table.add(i)
        return False