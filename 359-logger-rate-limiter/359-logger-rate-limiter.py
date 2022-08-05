class Logger(object):

    def __init__(self):
        self.most_recent_print_time = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.most_recent_print_time or self.most_recent_print_time[message] + 10 <= timestamp:
            self.most_recent_print_time[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)