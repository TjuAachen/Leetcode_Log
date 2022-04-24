class UndergroundSystem:

    def __init__(self):
        #record time, station
        self.ID_start = dict()
   #     self.ID_leave = dict()
        self.start_end = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ID_start[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.ID_start[id][0]
        start_time = self.ID_start[id][1]
        if (start,stationName) in self.start_end:
            self.start_end[(start,stationName)].append(t - start_time)
        else:
            self.start_end[(start,stationName)] = [t - start_time]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.start_end[(startStation,endStation)])/len(self.start_end[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)