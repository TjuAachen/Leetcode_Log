class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right=min(weights),sum(weights)
        n=len(weights)
        def check(capacity):
            sum_temp=0
            ans=0
            for i in range(n):
                sum_temp=sum_temp+weights[i]
                if sum_temp>capacity:
                    if capacity<weights[i]:
                        return -1
                    else:
                        sum_temp=weights[i]
                        ans=ans+1
            return ans+1
        while(left<right):
            mid=left+(right-left)//2
            if check(mid)<=days and check(mid)!=-1:
                right=mid
            elif check(mid)>days or check(mid)==-1:
                left=mid+1
        return left
                    