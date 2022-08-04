class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        #remove duplicates
        counting_point = set()
      #  point1, point2 = None, None
        y_set = defaultdict(set)
        for x, y in points:
            counting_point.add((x,y))
            y_set[y].add(x)
        
        y_line = None
        for key, x_list in y_set.items():
            if y_line == None:
                y_line = sum(x_list) / len(x_list)
                break
        for point in counting_point:
            reflected_point = [0, point[1]]
            reflected_point[0] =2 * y_line - point[0]
            reflected_point = tuple(reflected_point)
            if reflected_point not in counting_point:
                return False
        return True


        
            