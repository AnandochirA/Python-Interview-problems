from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        index1 = m - 1
        index2 = n - 1
        index_merge = m + n - 1
        
        # Merge nums2 into nums1 from the end
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[index_merge] = nums1[index1]
                index1 -= 1
            else:
                nums1[index_merge] = nums2[index2]
                index2 -= 1
            index_merge -= 1
        
        # If there are remaining elements in nums2, copy them
        while index2 >= 0:
            nums1[index_merge] = nums2[index2]
            index2 -= 1
            index_merge -= 1
