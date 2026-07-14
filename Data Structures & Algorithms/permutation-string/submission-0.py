class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        l=0
        r=k-1
        c,s2_c={},{}
        for i in s1:
            c[i]=c.get(i,0)+1
        ss=s2[l:k]
        for j in ss:
            s2_c[j]=s2_c.get(j,0)+1
        for i in range(r+1,len(s2)):
            if c==s2_c:
                return true
            s2_c[l]-=1
            l+=0
            s2_c[r]+=1
    
           

          
