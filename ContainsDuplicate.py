from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for i in range (0, len(nums)):
            if nums[i] in counts:
                return True
            else:
                counts[nums[i]] = 1
        return False
    
#I used just a dictionary, it is like using map in C++