# 151 Reverse Words in a String
class Solution1(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])

class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = []
        i = 0
        while i < len(s):
            if s[i] != " ":
                j = i + 1
                while j < len(s):
                    if s[j] == " ":
                        break
                    j += 1
                sList.append(s[i: j])
                i = j
            i += 1
        return " ".join(sList[::-1])
                
                    
# follow up
# 186 Reverse Words in a String II
class Solution_followUp(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: None Do not return anything, modify str in-place instead.
        """
        # reverse the whole string
        # reverse each word
        def reverse(l, r):
            while 0 <= l < r < len(str):
                str[l], str[r] = str[r], str[l]
                l += 1
                r -= 1
            return


        # corner case
        if not str:
            return

        reverse(0, len(str) - 1)

        l = 0
        for r in range(len(str)):
            if r != 0 and str[r] == " ":
                reverse(l, r - 1)
                l = r + 1
            elif r == len(str) - 1:
                reverse(l, r)
        return 
