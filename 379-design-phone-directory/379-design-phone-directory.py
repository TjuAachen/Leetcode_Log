class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        :type maxNumbers: int
        """
        self.used_nums = set()
        self.not_used_nums = list(range(maxNumbers))
        

    def get(self):
        """
        :rtype: int
        """
        if not self.not_used_nums:
            return -1
        popped = self.not_used_nums.pop()
        self.used_nums.add(popped)
        return popped
        

    def check(self, number):
        """
        :type number: int
        :rtype: bool
        """
        if number in self.used_nums:
            return False
        return True
        

    def release(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.used_nums:
            self.used_nums.remove(number)
         #   print(number, self.used_nums)
            self.not_used_nums.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)