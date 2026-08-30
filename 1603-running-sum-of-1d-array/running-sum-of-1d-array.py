class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_array=[]
        current_sum=0
        for num in nums:
            current_sum+=num
            sum_array.append(current_sum)
        return sum_array

        