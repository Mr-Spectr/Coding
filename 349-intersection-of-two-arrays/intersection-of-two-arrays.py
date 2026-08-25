class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
         set1 = set(nums1)
         result_set = set()
         for num in nums2:
            if num in set1:
                result_set.add(num)

         return list(result_set)
        