# 242 Valid Anagram

# sort
# Time: O(nlogn)
# Space: O(n)
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sList = sorted(list(s))
        tList = sorted(list(t))
        return sList == tList



# hashtable 1
# table
# Time: O(n)
# Space: O(1)
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        for c in counter:
            if c != 0:
                return False

        return True


# hashtable 2
class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        table = [0] * 26
        for i in range(len(s)):
            table[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            table[ord(t[i]) - ord('a')] -= 1
            if table[ord(t[i]) - ord('a')] < 0:
                return False

        return True
