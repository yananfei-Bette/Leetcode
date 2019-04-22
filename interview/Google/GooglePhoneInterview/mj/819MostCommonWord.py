# 819 Most Common Word

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        count = collections.Counter(
            word.strip("!?',;.") for word in paragraph.lower().split()
        )
        
        res, best = '', 0
        for word in count:
            if count[word] > best and word not in banned:
                res = word
                best = count[word]
        return res
        
        
        