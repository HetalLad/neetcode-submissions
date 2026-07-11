class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        arr={'}':'{',')':'(',']':'['}
        for i in s:
            if i not in arr:
                stack.append(i)
            elif stack and (arr[i]==stack[-1]):
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
     