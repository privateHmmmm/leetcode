# -*- coding:utf-8 -*-


# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
#
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
#
# Related problem: Reverse Integer
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        """
        binary=bin(n)
        lists=list(binary[2:])
        lists.reverse()
        lists += ['0' for i in range(0, 32-len(lists))]
        return eval('0b'+''.join(lists))
        """
        
        """
        for i in range(0, 16):
            low = (n>>i)&1
            high = (n>>31-i)&1
            
            if low!=high:
                n ^= ((1<<(31-i))|(1<<i))
        return n
        """ 
        
        """
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)   
        """
        
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
        """
        
        res = 0
        for i in range(0, 32):
            res <<=  1
            res += (n & 1)
            n >>= 1
        return res
            
