from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = sorted(nums)
        l = 0
        r = len(nums) - 1
        
        while(l != r):
            if(nums1[l] + nums1[r] == target):
                break
            elif nums1[l] + nums1[r] < target:
                l += 1
            elif nums1[l] + nums1[r] > target:
                r -= 1
                
        first = False
        second = False
        
        for i in range (0, len(nums)):
            if(nums1[l] == nums[i] and first == False):
                l = i
                first = True
            elif(nums1[r] == nums[i] and second == False):
                r = i
                second = True
            if(first and second):
                break;
                
        return [l, r]