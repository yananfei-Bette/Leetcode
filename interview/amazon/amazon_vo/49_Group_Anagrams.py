# 49 Group Anagrams

# Categorize by Sorted String
# Time: O(NKlogK)
# Spce: O(NK)
class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # corner case
        if not strs:
            return []

        dic = {}
        for str in strs:
            strSetKey = tuple(sorted(str))
            dic[strSetKey] = dic.get(strSetStr, []) + [str]
        return dic.values()


# Categorize by Count
# Time: O(kn)
# Space: O(kn)
class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
            
        dic = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            dic[tuple(count)] = dic.get(tuple(count), []) + [str]
        return dic.values()