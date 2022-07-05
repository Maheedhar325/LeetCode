class Solution:
    def isPalindrome(self, s: str) -> bool:
        sample_str = ''.join(c for c in s if c.isalnum())
        reverse = sample_str[::-1]
        if sample_str.lower() == reverse.lower():
            return True
        else:
            return False
        