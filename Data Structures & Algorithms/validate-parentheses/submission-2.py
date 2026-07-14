class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        arr={'}':'{',')':'(',']':'['}
        for i in s:
            if i not in arr:
                stack.append(i)
            elif (arr[i]==stack[-1]):
                stack.remove(arr[i])
            else:
                return False
        if not stack:
            return True
     