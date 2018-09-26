# 277 Find the Celebrity

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [i for i in xrange(n)]
        while len(stack) > 1:
            p1 = stack.pop()
            p2 = stack.pop()
            if knows(p1, p2):
                stack.append(p2)
            else:
                stack.append(p1)
                
        c = stack.pop()
        for i in xrange(n):
            if i != c and (knows(c, i) or not knows(i, c)):
                return -1
        return c