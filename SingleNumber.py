from typing import List 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range (0, len(nums)):
            answer = answer ^ nums[i];
        return answer
    
#Using XOR ^ which one is helped me to solve it in linear run time.