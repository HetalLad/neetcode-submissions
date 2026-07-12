import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=0
        op={'+':operator.add,
             '-':operator.sub,
             '*':operator.mul,
             '/': lambda a,b: int(operator.truediv(a,b))
        }
        stack=[]
        for i in tokens:
            if i in op:
                n2=int(stack.pop())
                n1=int(stack.pop())
                res= op[i](n1,n2)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]