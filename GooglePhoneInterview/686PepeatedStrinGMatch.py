#686 Repeated String Match
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        # find the min length of A that B in A.
        # reduced the problem to deciding whether B is a substring of some A * k
        # the tricky part is the value of q
        q = (len(B)-1)//len(A)+1
        print q, (len(B)-1)//(len(A)+1)
        for i in range(2):
            if B in A*(q+i): return q+i
        return -1
