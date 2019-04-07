# fizzbuzz
# leetcode 412

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            curr = ""
            if i % 3 == 0:
                curr += "Fizz"
            if i % 5 == 0:
                curr += "Buzz"
            if not curr:
                curr = str(i)
            res.append(curr)
        return res