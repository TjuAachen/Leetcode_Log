# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    """
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def __init__(self):
        self.cache = [' '] * 4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        cur = 0
        flag = True
        num_of_read_str = 0
        
        buf[:] = [' '] * n
        while(cur < n and self.count(self.cache) > 0):
            buf[cur] = self.cache.pop(0)
            cur += 1
            num_of_read_str += 1
        
        
        while(flag and cur < n):
            temp = [' ']*4
            read4(temp)
            flag, cur, temp_cur = self.write(temp, buf, cur, n)
            num_of_read_str += self.count(temp)
        
        
        buf[:] = buf[:cur]
        
        
        if cur == n and num_of_read_str > n:
            self.cache = temp[temp_cur:]
            
    def write(self, temp, buf, cur, n):
        
        for ind, elem in enumerate(temp):
            if elem == ' ' or cur == n:
                return False, cur, ind
            buf[cur] = elem
            cur += 1
        return True, cur, ind + 1
    def count(self, temp):
        ans = 0
        for elem in temp:
            if elem != ' ':
                ans += 1
        return ans
        