class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        mas = [i for i in sentence.split()]
        for i in range(len(mas)):
            if searchWord in mas[i][0: len(searchWord)]:
                return i + 1
        return -1
