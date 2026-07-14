class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val={}
        for i in nums:
            if i not in val:
                val[i]=1
            else:
                val[i]+=1
                return True 
        return False