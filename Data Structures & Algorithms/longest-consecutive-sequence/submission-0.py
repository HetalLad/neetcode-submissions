class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         nums.sort()
         sub=[]
         for i in nums:
            if i+1 in nums and i not in sub:
               sub.append(i)     
         return len(sub)+1

