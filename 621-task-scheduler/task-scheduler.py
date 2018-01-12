# -*- coding:utf-8 -*-


# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle. 
#
# You need to return the least number of intervals the CPU will take to finish all the given tasks.
#
# Example 1:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
#
#
# Note:
#
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
#
#


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = {}
        for task in tasks:
            task_count[task] = task_count.get(task, 0) + 1

        counts = task_count.values()
        counts.sort(reverse=True)

        start_index = 0
        while start_index < len(counts):

            if counts[start_index] > 1:
                idles=n - (len(counts) - 1 - start_index)
                if idles < 0:
                    i=start_index+n+1
                    while i<len(counts):
                        if counts[start_index]-1>=counts[i]:
                            break
                        i +=1
                    counts.insert(i, counts[start_index]-1)
                else:
                    idles = n - (len(counts) - 1 - start_index)
                    for i in range(0, idles):
                        counts.append(-1)  # -1 means  idle
                    counts.append(counts[start_index]-1)
            start_index += 1

        return len(counts)
    
