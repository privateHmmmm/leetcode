# -*- coding:utf-8 -*-


#
# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
#
#
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
#
#
#
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
#
#
#
# Note:
# The read function may be called multiple times.
#


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def __init__(self):
        
        self.point = 0    
        self.tmp = [""] * 4
        self.cnt = 0
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
        index = 0
        while index < n:
            
            if self.point == 0:
                self.cnt = read4(self.tmp)
                
            if self.cnt == 0: break
                
            for i in range(0, self.cnt-self.point):
                if index < n:
                    buf[index] = self.tmp[self.point]
                    index += 1
                    self.point += 1
                else:
                    break
                    
            if self.point == self.cnt: 
                self.point = 0
        
        return index
