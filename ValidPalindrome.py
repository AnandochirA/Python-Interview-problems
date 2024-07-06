import re

class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        # using regex to removing all non - alphanumeric characters and converting lowercase
        cleaned_string = re.sub(r'[\W_]+', '', s).lower()
        #just checking palindrome
        return cleaned_string == cleaned_string[::-1]