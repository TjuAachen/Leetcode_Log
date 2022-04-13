class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = list(a), list(b)
        len_a, len_b = len(a), len(b)
        long_len, short_len = max(len_a,len_b), min(len_a,len_b)
        arr = [0]*(long_len+1)
        a.reverse()
        b.reverse()
        for i in range(long_len):
            a_digit, b_digit = 0, 0
            carry = 0
            if i < len_a:
                a_digit = int(a[i])
            if i < len_b:
                b_digit = int(b[i])
            arr[i+1] = (a_digit + b_digit+arr[i])//2
            arr[i] = (a_digit + b_digit+arr[i])%2
        for i in range(long_len,-1,-1):
            if arr[i] == 0:
                arr.pop()
            else:
                break
        if not arr:
            arr.append(0)
        return ''.join([str(arr[i]) for i in range(len(arr)-1,-1,-1)] )
        
        