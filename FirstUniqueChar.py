class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        l = len(s)
        for i in range (0, l):
            if(s[i] in count):
                count[s[i]] += 1
            else:
                count[s[i]] = 1
                
        for i in range (0, len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1