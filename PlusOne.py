from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        while(index >= 0):
            if(digits[index] == 9):
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                break
        if(digits[0] == 0):
            digits[0] = 1
            digits.append(0)
        return digits