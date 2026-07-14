class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val={}
        l=[]
        for i in nums:
            if i not in val:
                val[i]=1
            else:
                val[i]+=1
        
        # Sort the items based on their frequency (value) in descending order
        sorted_items = sorted(val.items(), key=lambda item: item[1], reverse=True)
        
        # Take the top k keys
        for i in range(k):
            l.append(sorted_items[i][0])

        return l