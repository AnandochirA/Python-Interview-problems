from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        answer = []
            
        for i in range (0, len(nums1)):
            if(nums1[i] in counts):
                counts[nums1[i]] += 1;
            else:
                counts[nums1[i]] = 1
        for i in range (0, len(nums2)):
            if nums2[i] in counts:
                if counts[nums2[i]] > 0:
                    answer.append(nums2[i])
                    counts[nums2[i]] -= 1
        return answer