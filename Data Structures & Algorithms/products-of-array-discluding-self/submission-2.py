class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        prefix=[1]
        suffix=[1]
        output=[]
        for i in range(1,l):
            prefix.append(prefix[i-1]*nums[i-1])
        for j in range(l-1,0,-1):
            suffix.append(suffix[-1]*nums[j])
        suffix.reverse()
        for i in range(0,l):
            output.append(prefix[i]*suffix[i])
        return output