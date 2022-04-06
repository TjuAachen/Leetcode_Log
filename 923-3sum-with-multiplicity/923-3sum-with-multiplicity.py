class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        arr.sort()
        def find(i,target):
            count = 0
            left, right = i, n - 1
            while(left < right):
                if arr[left] + arr[right] == target:
                    p, q = left, right
                    count_left, count_right = 0, 0
                    while(p < right and arr[p] == arr[left]):
                        count_left += 1
                        p = p + 1
                    while(q > left and arr[q] == arr[right]):
                        count_right += 1
                        q = q - 1
                    if arr[left] == arr[right]:
                        count += (count_left+1)*count_left//2
                    else:
                        count += count_left*count_right
                    left, right = p, q
                elif arr[left] + arr[right] < target:
                    left = left + 1
                else:
                    right = right - 1
            return count
        final = 0
        for i in range(n):
            newTarget = target - arr[i]
            final += find(i+1, newTarget)
        return final%(10**9+7)
            
        