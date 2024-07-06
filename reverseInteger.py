class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        multiple = 1
        if (x < 0): multiple = -1
        x = abs(x)
        
        while x != 0:
            answer = answer * 10 + (x % 10)
            x = x // 10
        
        if answer < -2**31 or answer > 2**31 - 1: return 0   
        return answer * multiple
            