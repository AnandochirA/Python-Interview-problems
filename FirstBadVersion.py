# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if(n == 1): return 1
        
        if(n == 2):
            if isBadVersion(1) == True:
                return 1
            else:
                return 2
        s = 1
        e = n
        while e - s > 1:
            middle = (s + e) // 2
            if(isBadVersion(middle) == True):
                e = middle
            else:
                s = middle
            if e - s == 1:
                if isBadVersion(s) == True:
                    return s
                else: 
                    return e
            