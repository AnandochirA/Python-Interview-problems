from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        l = len(needle)
        for i in range(0, len(haystack) - l + 1):
            for j in range(0, l):
                if haystack[i + j] != needle[j]:
                    break
                if j == l - 1 and haystack[i + j] == needle[j]:
                    return i
        return -1
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        answer = ""
        for j in range(0, len(strs[0])):
            x = answer + strs[0][j]
            for i in range(1, len(strs)): 
                if self.strStr(strs[i], x) != 0:
                    return answer
            answer = x
        return answer
