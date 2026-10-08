class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        start = 0
        end = len(s)-1
        while(start < end):
            a = s[start]
            b = s[end]
            if(a == b or a.upper() == b or a.lower() == b):
                start+=1
                end-=1
                continue
            else:
                return False
        return True
