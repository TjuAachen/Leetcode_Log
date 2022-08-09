class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        bucket = defaultdict(int)
        key = []
        for num in nums:
            if num not in bucket:
                key.append(num)
            bucket[num] += 1
        n = len(key)
        
        def is_single_divisor(num1, num2, num3):
            if num1 == num2 == num3:
                return False
            sum_nums = num1 + num2 + num3
            a1 = sum_nums%num1
            a2 = sum_nums%num2
            a3 = sum_nums%num3
            if a1 == 0 and a2 != 0 and a3 != 0:
                return True
            if a2 == 0 and a1 != 0 and a3 != 0:
                return True
            if a3 == 0 and a2 != 0 and a1 != 0:
                return True
            return False
       # key.sort()
        count = 0
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    num1, num2, num3 = key[i], key[j], key[k]
                 #   print(num1, num2, num3)
                    if is_single_divisor(num1, num2, num3):
                        if num1 != num2 and num2!= num3 and num3 != num1:
                            count += bucket[num1] * bucket[num2] * bucket[num3] * 6
                        elif num1 == num2:
                            count += bucket[num1] * (bucket[num2] - 1) * bucket[num3] * 3
                        elif num1 == num3:
                            count += bucket[num1] * (bucket[num3] - 1) * bucket[num2] * 3   
                        elif num2 == num3:
                            count += bucket[num2] * (bucket[num3] - 1) * bucket[num1] * 3                  
        return count
                        
        
        