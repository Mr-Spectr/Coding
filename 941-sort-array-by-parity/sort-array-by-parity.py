class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        x=[]
        for i in nums:
            if i%2==0:
                x.insert(0, i)
            else:
                x.append(i)
        return x
        