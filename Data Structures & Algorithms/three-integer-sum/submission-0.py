class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol=list()
        for i in range(0,len(nums)):
            a=nums[i]
            if (a>0):
                break
            l=i+1
            r=len(nums)-1
            while (l < r):
                if (nums[l] + nums[r] == (-1 *a)):
                    sol.append([a,nums[l],nums[r]])
                    break;
                elif (nums[l] + nums[r] < (-1 *a)):
                    l+=1
                else:
                    r-=1
            return sol

