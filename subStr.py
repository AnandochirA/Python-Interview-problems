class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(haystack == needle): return 0
        l = len(needle)
        for i in range(0, len(haystack) - l + 1):
            for j in range (0, l):
                if(haystack[i + j] != needle[j]):
                    break
                if(j == l - 1 and haystack[i + j] == needle[j]):
                    return i
        return -1