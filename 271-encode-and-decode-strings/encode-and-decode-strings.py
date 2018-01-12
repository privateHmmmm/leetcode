# -*- coding:utf-8 -*-


#
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
#
# Machine 1 (sender) has the function:
#
# string encode(vector&lt;string&gt; strs) {
#   // ... your code
#   return encoded_string;
# }
#
# Machine 2 (receiver) has the function:
#
# vector&lt;string&gt; decode(string s) {
#   //... your code
#   return strs;
# }
#
#
#
# So Machine 1 does:
# string encoded_string = encode(strs);
#
#
#
# and Machine 2 does:
# vector&lt;string&gt; strs2 = decode(encoded_string);
#
#
#
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
#
# Implement the encode and decode methods.
#
#
# Note:
#
# The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
#


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        
        res = ""
        for _str in strs:
            res += (str(len(_str)) + '/' + _str)

        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        
        res = []
        i = 0
        while i < len(s):
            index = s.index("/", i)
            lens = int(s[i:index])
            res.append(s[index+1:index+1+lens])
            i = index + 1 + lens
            
        return res
            
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
