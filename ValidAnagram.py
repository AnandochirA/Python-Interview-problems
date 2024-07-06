class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        first = {}
        second = {}
        
        for i in range(0, len(s)):
            if(s[i] in first):
                first[s[i]] += 1
            else:
                first[s[i]] = 1
        
        for i in range(0, len(t)):
            if(t[i] in second):
                second[t[i]] += 1
            else:
                second[t[i]] = 1
        
        for i in range (0, len(s)):
            if(s[i] not in second):
                return False
            if(first[s[i]] != second[s[i]]):
                return False
        return True