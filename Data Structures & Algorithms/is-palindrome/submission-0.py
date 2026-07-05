class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        left=0
        right=len(s)-1
        while (left < right):
            if(s[left] == s[right]):
                right-=1
                left+=1
                continue
            else:
                return False
        return True