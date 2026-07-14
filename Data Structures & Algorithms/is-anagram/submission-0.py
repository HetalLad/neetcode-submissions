class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val1={}
        val2={}
        for i in s:
            if i not in val1:
                val1[i]=1
            else:
                val1[i]+=1
        
        for j in t:
            if j not in val2:
                val2[j]=1
            else:
                val2[j]+=1

    
        sorted_v1= dict(sorted(val1.items()))
        sorted_v2= dict(sorted(val2.items()))
        if sorted_v1==sorted_v2:
            return True 
        else:
            return False
