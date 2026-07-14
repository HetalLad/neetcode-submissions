class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            l=len(i)
            result+= str(l)
            for j in i:
                result+= "#"+i
        return result

    def decode(self, s: str) -> List[str]:
        val=[]
        for i in s:
            if i.isdigit():
                l=num(i)
                c=0
                w=''
                continue
            else:
                w+=i
                while(c<l): c+=1
            val.append(w)
        return val    


