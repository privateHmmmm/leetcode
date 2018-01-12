# -*- coding:utf-8 -*-


# An abbreviation of a word follows the form &lt;first letter&gt;&lt;number&gt;&lt;last letter&gt;. Below are some examples of word abbreviations:
#
# a) it                      --> it    (no abbreviation)
#
#      1
# b) d|o|g                   --> d1g
#
#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
#
#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
#
#
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
#
# Example: 
#
# Given dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
#
#


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        
        self._map = {}
        for word in dictionary:
            key = self.getAbb(word)
            if key in self._map:
                if self._map[key] != word:
                    self._map[key] = None
            else:
                self._map[key] = word
       
    def getAbb(self, word):
        
        if len(word) <= 2:
            return word
        
        return word[0]+str(len(word)-2)+word[-1]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """

        key = self.getAbb(word)
        if key not in self._map or self._map[key] == word:
            return True
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
