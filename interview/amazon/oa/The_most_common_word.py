# The most common word
# leetcode 819

# https://leetcode.com/problems/most-common-word/submissions/
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
            
        count = collections.Counter(
            word for word in paragraph.lower().split()
        )
        
        res, best = '', 0
        for word in count:
            if count[word] > best and word not in banned:
                res = word
                best = count[word]
        return res
    
        
        
        