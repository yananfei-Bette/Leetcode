# 205 Isomorphic String
# idea comes form:https://leetcode.com/problems/isomorphic-strings/discuss/155904/Python-dictionaries
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        dic1, dic2 = {}, {}
        for i,val in enumerate(s):
            dic1[val] = dic1.get(val,[])+[i]
        for i,val in enumerate(t):
            dic2[val] = dic2.get(val,[])+[i]
        #print dic1,dic2
        #print sorted(dic1.values()), sorted(dic2.values())
        return sorted(dic1.values()) == sorted(dic2.values())
        '''
        # pair
        if len(s) != len(t): return False
        dic_s, dic_t = {}, {}
        for i, (char_s, char_t) in enumerate(zip(s,t)):
            if char_s not in dic_s:
                dic_s[char_s] = i
            if char_t not in dic_t:
                dic_t[char_t] = i
            if dic_s[char_s] != dic_t[char_t]: return False
        return True
        
