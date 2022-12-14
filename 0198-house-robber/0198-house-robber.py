class Solution:
    def rob(self, nums: List[int]) -> int:
        f=[0]*len(nums)
        for j in range(len(nums)):
            if j==0:
                f[0]=nums[0]
            elif j==1:
                f[1]=max(nums[0],nums[1])
            else:
                if f[j-1]==f[j-2]:
                    f[j]=f[j-1]+nums[j]
                else:
                    f[j]=max(f[j-2]+nums[j],f[j-1])
        return f[len(nums)-1]
                