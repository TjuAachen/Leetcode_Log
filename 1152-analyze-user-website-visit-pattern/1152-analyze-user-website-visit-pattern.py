class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        track = []
        record = dict()
        length = 0
        username =[i  for _,i in sorted(zip(timestamp,username))]
        website =[i  for _,i in sorted(zip(timestamp,website))]
        data = dict()
        for ind,user in enumerate(username):
            if user in data:
                data[user].append(website[ind])
            else:
                data[user] = [website[ind]]
        def store(start):
            if len(track) == 3 and tuple(track) not in visited:
                if tuple(track) not in record:
                    record[tuple(track)] = 1
                else:
                    record[tuple(track)] += 1
                visited[tuple(track)] = 1
                return
            elif len(track) == 3:
                return
            for i in range(start,length):
                track.append(pattern[i])
                store(i+1)
                track.pop()
        pattern = []
        n = len(website)
        for key,value in data.items():
            length = len(value)
            if length >= 3:
                pattern[:] = value
                visited = dict()
                store(0)
                
        max_value = -float(inf)
        value_set = []
        for key, val in record.items():
            if val >= max_value:
                if value_set and record[value_set[-1]] <val:
                    value_set = []
                value_set.append(key)
                max_value = val
        if len(value_set) == 1:
            return list(value_set[0])
        elif len(value_set) > 1:
            return sorted(list(value_set))[0]
        else:
            return 
                
                
            
            
        