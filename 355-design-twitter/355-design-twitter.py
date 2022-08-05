from sortedcontainers import SortedList
from heapq import *
class Twitter:

    def __init__(self):
        self.user_followers = defaultdict(set)
        self.user_followee = defaultdict(set)
        
        self.user_post_tweet = defaultdict(deque)
        self.tweetId_userId = defaultdict(int)

        self.cur_time = 0

        self.user_news_feed = defaultdict(list)
        self.user_news_feed_time = defaultdict(SortedList)
        self.user_follower_pointer = defaultdict(int)
        
        self.tweet_time = defaultdict(int)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [self.cur_time, tweetId, userId]
        self.tweetId_userId[tweetId] = userId
        self.tweet_time[tweetId] = self.cur_time
        self.cur_time += 1
        self.user_post_tweet[userId].appendleft(tweet)
        self.user_followers[userId].add(userId)
        self.user_followee[userId].add(userId)
      #  self.user_follow_who[userId].add(userId)
        self.updateNewsFeed_by_tweet(tweet)
        #self.user_follower_pointer = defaultdict(int)
    
    def updateNewsFeed_by_tweet(self, tweet):
        tweet_time, tweetId, userId = tweet
        
        followers = self.user_followers[userId]
        
      #  print(followers, userId)
        for follower in followers:
            res = self.user_news_feed[follower]
            res_time = self.user_news_feed_time[follower]
            if len(res) == 10 and tweet_time < - res_time[-1]:
                continue
            self.user_follower_pointer[(follower, userId)] += 1
            index = res_time.bisect_left(-tweet_time)
            if len(res) == 10:
                popped = res.pop()
                res_time.pop()
                popped_userId = self.tweetId_userId[popped]
                self.user_follower_pointer[(follower, popped_userId)] -= 1
            res_time.add(-tweet_time)
            res = res[:index] + [tweetId] + res[index:]
            self.user_news_feed[follower] = res
            self.user_news_feed_time[follower] = res_time
       #     print(res, follower)
    
    def updateNewsFeed_by_add_followee(self, userId, followerId):
        res = self.user_news_feed[followerId]
        res_time = self.user_news_feed_time[followerId]
        i = self.user_follower_pointer[(followerId, userId)]
        n = len(self.user_post_tweet[userId])

        for j in range(i,n):
            tweet = self.user_post_tweet[userId][j]
            tweet_time, tweetId, _ = tweet
            
            if len(res) == 10 and res_time and tweet_time < - res_time[-1]:
                break
            index = res_time.bisect_left(-tweet_time)
            self.user_follower_pointer[(followerId, userId)] += 1
            if len(res) == 10:
                popped = res.pop()
                res_time.pop()
                popped_userId = self.tweetId_userId[popped]
                self.user_follower_pointer[(followerId, popped_userId)] -= 1
            res_time.add(-tweet_time)
            res = res[:index] + [tweetId] + res[index:]
        self.user_news_feed[followerId] = res
        self.user_news_feed_time[followerId] = res_time
        #print(res, followerId)
                
    def updateNewsFeed_by_remove_followee(self, userId, followeeId):

        res = self.user_news_feed[userId]
        res_time = self.user_news_feed_time[userId]

        in_side = self.user_follower_pointer[(userId, followeeId)]
      #  print(in_side, userId, followeeId, self.user_news_feed[userId])
        if in_side == 0:
            return
        #print(self.user_post_tweet[userId])
        i = 0
        cur_list = []
        while(i < in_side):
            cur_list.append(self.user_post_tweet[followeeId][i][1])
            i += 1
        #print(cur_list)
        #remove the tweets from the follower
        #print(cur_list, res)
        new_res = []
        for i, elem in enumerate(res):
            if elem in cur_list:
                res_time.remove(-self.tweet_time[elem])
            else:
                new_res.append(elem)
        del self.user_follower_pointer[(userId, followeeId)]
        
        self.user_news_feed[userId] = new_res
        self.user_news_feed_time[userId] = res_time
        
        #add new posts from other followers
        for followee in self.user_followee[userId]:
           # print(self.user_news_feed_time[userId], self.user_post_tweet[userId])
            self.updateNewsFeed_by_add_followee(followee, userId)
        
        
        
    def getNewsFeed(self, userId: int) -> List[int]:
     #   print(self.user_news_feed)
        return self.user_news_feed[userId]
        
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followers[followeeId]:
            self.user_followers[followeeId].add(followerId)
            self.user_followee[followerId].add(followeeId)
            self.updateNewsFeed_by_add_followee(followeeId, followerId)   
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followers[followeeId]:
            self.user_followers[followeeId].remove(followerId)
            self.user_followee[followerId].remove(followeeId)
            self.updateNewsFeed_by_remove_followee(followerId, followeeId)             
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)