class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=""
        for i in range(max(len(word1), len(word2))):
            if i<len(word1):
                new=new+word1[i]
            if i<len(word2):
                new=new+word2[i]

        return new

        