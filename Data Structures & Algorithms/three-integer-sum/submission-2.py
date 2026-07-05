class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol=[]
        for i in range(0,len(nums)):
            a=nums[i]
            if (a>0):
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l=i+1
            r=len(nums)-1
            while (l < r):
                if (nums[l] + nums[r] == (-1 *a)):
                    sol.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif (nums[l] + nums[r] < (-1 *a)):
                    l+=1
                else:
                    r-=1
        return sol

