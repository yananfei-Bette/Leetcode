class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # Amazon OA right rotation
        if len(A) != len(B):
            return False
        if not A:
            return True
        string = A + A
        return True if B in string else False