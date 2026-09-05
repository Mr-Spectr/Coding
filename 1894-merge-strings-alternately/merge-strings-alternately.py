class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=len(word1)
        w2=len(word2)
        m=max(w1,w2)
        new=""
        for i in range(m):
            if i<w1:
                new=new+word1[i]
            if i<w2:
                new=new+word2[i]

        return new

        