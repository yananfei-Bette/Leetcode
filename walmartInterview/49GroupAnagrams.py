# 49 Group Anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        '''
        # time : 0(n*k*logk)
        if not strs:
            return [[]]
        
        dic = {}
        for s in strs:
            sSet = tuple(sorted(s))
            if sSet not in dic:
                dic[sSet] = [s]
            else:
                dic[sSet].append(s)
                
        res = []
        for key, val in dic.items():
            res.append(val)
        return res
        '''
        if not strs: return [[]]
        dic = {}
        for s in strs:
            count = [0] * 26
            for sElement in s:
                count[ord(sElement) - ord('a')] += 1
            sSet = tuple(count)
            if sSet not in dic:
                dic[sSet] = [s]
            else:
                dic[sSet].append(s)
        return dic.values()