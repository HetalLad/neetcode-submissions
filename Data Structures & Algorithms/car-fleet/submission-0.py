class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_a=[(i,j) for i,j in zip(position,speed)]
        combined_a.sort(key=lambda x: x[0], reverse=True)
        tt=0
        stack=[]
        for i,j in combined_a:
            tt=(target-i)/j
            stack.append(tt)
            if len(stack) >=2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)




        