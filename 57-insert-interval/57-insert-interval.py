class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = [[-2,-1]]+intervals
        def findLeft(target):
            left, right = 0, len(intervals) 
            while(left < right):
                mid = left + (right - left)//2
                if (intervals[mid][0] >= target):
                    right = mid
                else:
                    left = mid + 1
            return left - 1
        def findRight(target):
            left, right = 0, len(intervals) 
            while(left < right):
                mid = left + (right - left)//2
                if (intervals[mid][0] <= target):
                    left = mid + 1
                else:
                    right = mid
            return left - 1
        l = findLeft(newInterval[0])
        r = findRight(newInterval[1])
        if l != 0:
            if newInterval[0] <= intervals[l][1]:
                left_part = min(intervals[l][0],newInterval[0])
                left_half = intervals[1:l]
            else:
                left_part = newInterval[0]
                left_half = intervals[1:l+1]
        else:
            left_part = newInterval[0]
            left_half = intervals[:l]
        if r != 0:
            
            right_part = max(intervals[r][1],newInterval[1])
        else:
            right_part = newInterval[1]
        right_half = intervals[r+1:]
        return left_half+[[left_part,right_part]]+right_half
 
            
            