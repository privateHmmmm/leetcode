# -*- coding:utf-8 -*-


# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:
#
#
#
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
#
#
#
# Example:
#
# Twitter twitter = new Twitter();
#
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
#
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
#
# // User 1 follows user 2.
# twitter.follow(1, 2);
#
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
#
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);
#
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
#
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
#
#


# import Queue

# class Tweet(object):
    
    # def __init__(self, userId, tweetId, timestamp):
        
        # self.userId = userId
        # self.tweetId = tweetId
        # self.timestamp = timestamp

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # self.tweets = collections.defaultdict(Queue.PriorityQueue())
        self.tweets = collections.defaultdict(list)
        self.cnt = 0
        self.followeeIds = collections.defaultdict(set)
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        
        self.cnt +=1
        # tweet = Tweet(userId, tweetId, self.cnt)
        # if userId not in self.tweets:
            # self.tweets[userId] = Queue.PriorityQueue()
        # self.tweets[userId].put([-tweet.timestamp, tweet])
        
        self.tweets[userId].append([self.cnt, tweetId])
        self.followeeIds[userId].add(userId)
        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        
        # tmpLists = []
        lists = []
        
        for user in self.followeeIds[userId]:
            # tmpLists[:] = []
            # while not self.tweets[user].empty():
            # while self.tweets[user]:
            lists.extend(self.tweets[user][-10:])
                
                # tweet = self.tweets[user].get()
                # tmpLists.append(tweet)
                
                # lists.append([tweet[0], tweet[1].tweetId])
                # if len(tmpLists) >=10:
                    # break
        
            # for tweet in tmpLists:
                # self.tweets[user].put(tweet)
    
        # print lists
        lists.sort(key=lambda items: items[0], reverse=True)
        # print lists
        return [a[1] for a in lists[0:10]]
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        
        self.followeeIds[followerId].add(followeeId)
        
    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        
        if followerId != followeeId and followeeId in self.followeeIds[followerId]:
            self.followeeIds[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
