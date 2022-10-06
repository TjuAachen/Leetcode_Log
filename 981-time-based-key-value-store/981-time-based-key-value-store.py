from sortedcontainers import SortedList
class TimeMap(object):

    def __init__(self):
        self.dataTimeStamp = defaultdict(SortedList)
        self.timeStampValue = defaultdict(dict)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dataTimeStamp[key].add(timestamp)
        self.timeStampValue[key][timestamp] = value
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.dataTimeStamp:
            return ""
        timeStamps = self.dataTimeStamp[key]
        idx = timeStamps.bisect(timestamp) - 1
        if idx < 0:
            return ""
        resTimeStamp = timeStamps[idx]
        return self.timeStampValue[key][resTimeStamp]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)