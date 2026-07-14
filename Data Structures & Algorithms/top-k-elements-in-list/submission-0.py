class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val={}
        l=[]
        for i in nums:
            if i not in val:
                val[i]=1
            else:
                val[i]+=1
        for key,v in val.items():
            if v>=k:
                l.append(key)
                
        return l