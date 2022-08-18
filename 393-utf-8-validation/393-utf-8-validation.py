class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n_bytes = 0
        mask1 = (1<<7)
        mask2 = (1<<6)
        for num in data:
            if n_bytes == 0:
                #begin
                new_mask = mask1
                while(num&new_mask):
                    n_bytes += 1
                    new_mask = (new_mask >> 1)
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not(mask1&num and not mask2&num):
                    return False
            n_bytes -= 1
        return n_bytes == 0
                
        