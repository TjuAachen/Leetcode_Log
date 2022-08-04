class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        if m>n:
            return 0
        dp = [0] * (n+1)
        nums = list(range(1,10))
        global count
        count = 0
        seen = set()
        middle = [2,4,6,8]
        corner = [1,3,7,9]
        center = 5
        graph = defaultdict(set)
        for i in corner:
            graph[center].add(i)
            for elem in middle:
                graph[i].add(elem)
            graph[i].add(center)
        
        for i in middle:
            graph[center].add(i)
            for elem in corner:
                graph[i].add(elem)
            if i == 4 or i == 6:
                graph[i].add(2)
                graph[i].add(8)
            else:
                graph[i].add(4)
                graph[i].add(6)
            graph[i].add(center)
       # print(graph)
        
        
        
        def get_num(step, prev):
            global count
            if n - step > 0:
                dp[n-step] += 1
            if step == 0:
              #  print(seen, prev)
                count += 1
                return
            for num in nums:
                if num in seen:
                    continue
                #print(prev,num)
                seen.add(num)
                if prev == None:
                    get_num(step-1, num)
                elif num in graph[prev]:
                    get_num(step-1, num)
                elif (num+prev)//2 in seen:
                    get_num(step-1, num)
                seen.remove(num)
        get_num(n, None)
        return sum(dp[m:n+1])
        
            
        
        
                
                
        