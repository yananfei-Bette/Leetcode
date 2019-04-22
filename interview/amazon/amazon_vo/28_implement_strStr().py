# 28 implement strStr()

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # brute borce
        # Time: O(m * n)

        '''
        # corner case
        if not needle:
            return 0

        if not haystack:
            return -1

        j = 0
        while j < len(haystack):
            if haystack[j] == needle[0]:
                i = 0
                while i + j < len(haystack) and i < len(needle):
                    if haystack[i + j] == needle[i]:
                        i += 1
                    else:
                        break

                if i + j <= len(haystack) and i == len(needle):
                    return j

            j += 1

        return -1
        '''

        i = 0
        while True:
            j = 0
            while True:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if needle[j] != haystack[i + j]:
                    break
                j += 1

            i += 1

        return -1







