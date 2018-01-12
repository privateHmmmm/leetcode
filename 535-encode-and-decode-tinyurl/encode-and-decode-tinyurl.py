# -*- coding:utf-8 -*-


# Note: This is a companion problem to the System Design problem: Design TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


class Codec:

    import string
    letters = string.ascii_letters + string.digits
    letter_lens = len(letters)
    dicts = {}
    global_counter = 0
    
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        def genStr(idx):
            
            res =""
            while 1:
                res += self.letters[idx%self.letter_lens]
                idx = idx/self.letter_lens
                if idx == 0:
                    break
            return res
        
        Str = genStr(self.global_counter)
        self.global_counter +=1
        self.dicts[Str] = longUrl
        return Str

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        return self.dicts[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
