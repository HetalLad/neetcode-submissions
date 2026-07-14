class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        arr={'}':'{',')':'(',']':'['}
        for i in s:
            if i not in arr:
                stack.append(i)
            else:
                stack.remove(arr[i])
        if not stack:
            return True
        else:
            return False