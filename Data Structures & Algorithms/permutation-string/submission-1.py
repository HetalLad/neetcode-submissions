class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        l=0
        c,s2_c={},{}
        ss=s2[l:k]
        for i in s1:
            c[i]=c.get(i,0)+1
        for j in ss:
            s2_c[j]=s2_c.get(j,0)+1
        if c == s2_c:
            return True
        for i in range(k,len(s2)):
            if(s2_c[s2[l]]==1):
                del s2_c[s2[l]]
            else:
                s2_c[s2[l]]-=1
            l+=1
            s2_c[s2[i]]=s2_c.get(s2[i],0)+1
            if c == s2_c:
                return True
                
        return False
           

          
