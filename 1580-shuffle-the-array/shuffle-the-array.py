class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x1=nums[:n]
        x2=nums[n:]
        ret=[]
        for i in range(0,n):
            ret.append(x1[i])
            ret.append(x2[i])
        return ret
        