class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window=[nums[i] for i in range(0,k)]
        l=0
        res=[max(window)]
        for r in range(k,len(nums)):
            window.remove(nums[l])
            l+=1
            window.append(nums[r])
            max_window_elem=max(window)
            res.append(max_window_elem)
        return res


