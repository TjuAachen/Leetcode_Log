from sortedcontainers import SortedDict
class Twitter(object):

    def __init__(self):
        #push-pull
        #push model here
        self.user_followees = defaultdict(set)
        self.user_tweetId = defaultdict(list) 
        self.time = 0
        
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.user_followees[userId]:
            self.user_followees[userId].add(userId)
        self.user_tweetId[userId].append([self.time, tweetId])
        self.time += 1
        
            
        
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        #pull
        res = SortedDict()
      #  print(self.user_followees[userId])
        for followee in self.user_followees[userId]:
            for time, tweetId in reversed(self.user_tweetId[followee]):
              #  print(time, userId, res)
                if len(res) < 10:
                    res[time] = tweetId
                else:
                    oldest_time, _ = res.peekitem(0)
                    if oldest_time > time:
                        break
                    res[time] = tweetId
                    res.popitem(0)

        final_res = deque()
        for time, tweetId in res.items():
            final_res.appendleft(tweetId)
        return list(final_res)

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self.user_followees[followerId]:
            self.user_followees[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.user_followees[followerId]:
            self.user_followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)