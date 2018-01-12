# -*- coding:utf-8 -*-


#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Return 4.
#
#
# Credits:Special thanks to @Freezen for adding this problem and creating all test cases.


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])

        """
        max_length = 0
        for i in range(0, row):
            for j in range(0, col):
                #print 'i: %d, j: %d' % (i, j)
                if matrix[i][j] == "1":
                    length = 1
                    while 1:
                        if length > max_length:
                            max_length = length

                        if i + length < row and j + length < col:
                            length += 1
                        else:
                            break
                        if "0" in [matrix[k][j + length - 1] for k in range(i, i + length)]:
                            break

                        if "0" in matrix[i + length - 1][j:j + length]:
                            break

        return max_length ** 2
        """
        
        pre = [0 if matrix[0][j]=='0' else 1 for j in range(0, col)]
        max_size=max(pre)

        for i in range(1, row):
            cur = [0 if matrix[i][0] == '0' else 1]
            for j in range(1, col):
                if matrix[i][j] == '1':
                    Size = min(cur[-1], pre[j - 1], pre[j]) + 1
                else:
                    Size = 0
                cur.append(Size)
            if max(cur) > max_size:
                max_size = max(cur)

            for j in range(0, col):
                pre[j] = cur[j]

        return max_size **2
    
