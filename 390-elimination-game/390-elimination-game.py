class Solution:
    def lastRemaining(self, n: int) -> int:
        count = n
        start = 1
        interval = 2
        is_start = True
        while(count > 1):
            
            if is_start:
                count = count // 2
                start = start + interval//2
            else:
                if count%2:
                    start = start + interval//2
                count = count//2
                    
          #  print(count, start, interval)
            interval *= 2
            is_start = not is_start
        return start
            