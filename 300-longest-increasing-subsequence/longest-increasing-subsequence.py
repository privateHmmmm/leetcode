# -*- coding:utf-8 -*-


#
# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
#
#
# Your algorithm should run in O(n2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity? 
#
# Credits:Special thanks to @pbrother for adding this problem and creating all test cases.


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # O(n^2), but TLE, I don't know why
        if not nums:
            return 0
        
        DP=[0 for i in range(0, len(nums))] # LIS include i
        DP[0]=1
        
        DP2=[0 for i in range(0, len(nums))] # LIS 
        DP2[0]=1
        
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                
                DP[i]=max(DP[i], (DP[j]+1 if nums[j]<nums[i] else 1))
        
        return max(DP)
        """ 
        """
        # O(nlog(n))
        if not nums:
            return 0
        
        _min = [max(nums)]*(len(nums)+1)
        max_len = 1
        _min[0] = min(nums)-1
        _min[1] = nums[0]
        
        for i in range(1, len(nums)):
            # for j in range(i-1, -1, -1):
            L = 1; R = max_len; ans = 0
            while L<=R:
                mid = (L+R)/2
                if _min[mid] < nums[i]:
                    ans = mid
                    L = mid + 1
                else:
                    R = mid - 1
            lens = ans + 1
            _min[lens] = min(_min[lens], nums[i])
            max_len = max(max_len, lens)
                
        return max_len
        """
    
        if not nums: return 0
        
        _min = [nums[0]]
        for i in range(1, len(nums)):
            L = 0; R = len(_min)-1 # need to calc the last one who is smaller than nums[i]
            ans = -1
            while L <= R:         
                mid = (L+R)/2
                if _min[mid] < nums[i]:
                    ans = mid
                    L = mid + 1
                else:
                    R = mid - 1
                
            ans +=1
            if ans > len(_min)-1:
                _min.append(nums[i])
            else:
                _min[ans] = nums[i]
        
        return len(_min)
            
