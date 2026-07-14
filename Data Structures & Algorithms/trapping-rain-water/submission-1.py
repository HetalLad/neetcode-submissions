class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefix=[]
        suffix=[0]*n
        area=[0]*n
        for i in range(0,n):
            if i==0 :
                prefix.append(height[0])
            else:
                prefix.append(max(prefix[i-1],height[i]))
        for j in range(n-1,0,-1):
            if(j==n-1):
                suffix[n-1]=height[n-1]
            else:
                suffix[j]= max(suffix[j+1],height[j])
        for i in range(0,n):
            area[i]=min(prefix[i],suffix[i])-height[i]
        print(prefix)
        print( suffix)
        print(area)
        return sum(area)