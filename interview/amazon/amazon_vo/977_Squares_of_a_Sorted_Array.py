# 977 Squares of a Sorted Array

# sort
# Time: O(nlogn)
# Space: O(n)
class Solution1(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # edge case
        if not A:
            return []
        return sorted([x * x for x in A])


# Two Pointers
# Time: O(n)
# Space: O(n)
class Solution2(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # edge case
        if not A:
            return []

        N = len(A)

        # get negative part and positive part
        j = 0
        while j < N and A[j] < 0:
            j += 1

        i = j - 1

        res = []
        while 0 <= i and j < N:
            if A[i] ** 2 < A[j] ** 2:
                res.append(A[i] ** 2)
                i -= 1
            else:
                res.append(A[j] ** 2)
                j += 1

        while i >= 0:
            res.append(A[i] ** 2)
            i -= 1
        while j < N:
            res.append(A[j] ** 2)
            j += 1

        return res















