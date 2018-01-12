# -*- coding:utf-8 -*-


# Shuffle a set of numbers without duplicates.
#
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
#
#



class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.lists = nums
        
        if not self.lists:
            return 
        
        self.fractorialDicts = {1: 1}
        def getFractorial(n):

            if n not in self.fractorialDicts:
                self.fractorialDicts[n] = n*getFractorial(n-1)
            return self.fractorialDicts[n]
        _ = getFractorial(len(self.lists))

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        
        return self.lists

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        
        if not self.lists:
            return []
        
        idx = random.randint(0, self.fractorialDicts[len(self.lists)]-1)
        def getList(lists, idx, res):
            
            if idx == 0:
                res.extend(lists)
                return

            ll = self.fractorialDicts[len(lists)-1]
            tmp = idx / ll
            res.append(lists[tmp])
            del lists[tmp]
            getList(lists, idx - tmp*ll, res)
        
        res = []
        list_copy = copy.copy(self.lists)
        getList(list_copy, idx, res)
        return res
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
