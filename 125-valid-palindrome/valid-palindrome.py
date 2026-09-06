class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_strip=re.sub(r'[^a-zA-Z0-9]','',s).lower()
        return s_strip==s_strip[::-1]
        