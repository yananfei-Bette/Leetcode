# Combinations with order

# Given two strings
# ouput all combinations without change string's order
# s1 = “AB”  s2 = “CD” 
# output: ABCD ACBD ACDB CABD CADB CDAB

class Solution(object):
    def permutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        def backtrack(s1, ind1, s2, ind2, curr):
            # boundary
            if len(curr) == len(s1) + len(s2):
                res.append(curr)
                return

            if ind1 < len(s1):
                backtrack(s1, ind1 + 1, s2, ind2, curr + s1[ind1])
            if ind2 < len(s2):
                backtrack(s1, ind1, s2, ind2 + 1, curr + s2[ind2])
            return

        # corner case
        if not s1:
            return s2
        if not s2:
            return s1

        res = []
        backtrack(s1, 0, s2, 0, "")
        return res

if __name__ == "__main__":
    s1 = "AB"
    s2 = "CD"
    sol = Solution()
    print(sol.permutation(s1, s2))
