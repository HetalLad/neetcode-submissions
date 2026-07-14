class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        p=1
        o=[1]*l
        for i in nums:
            p*=i
        for i in range(0,l):
            o[i]= int(p/nums[i])
        return o