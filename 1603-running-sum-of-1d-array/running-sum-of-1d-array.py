class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i=0
        x=[]
        for a in nums:
            i=i+a
            x.append(i)
        return x
        