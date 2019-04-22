# [1, 2, 3, 1, 3]
# count how many elements which are duplicated
def countNums(nums):
    # time: O(n + m)
    # space: O(n)
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    res = 0
    for v in dic.values():
        if v > 1:
            res += 1
    return res

def validParenthese(str):
    stack = []
    for char in str:
        if char in {"(", "[", "{"}:
            stack.append(char)
        elif stack and (
            (char == ")" and stack[-1] == "(") or 
            (char == "]" and stack[-1] == "[") or 
            (char == "}") and stack[-1] == "{"):
            stack.pop()
        else:
            return False
    return not stack

class Solution(object):
    def isValidIPv4(self, IP):
        if len(IP) < 7:
            return False
        if IP[0] == ".":
            return False
        if IP[-1] == ".":
            return False
        tokens = IP.split(".")
        if len(tokens) != 4:
            return False
        for token in tokens:
            # print self.isValidIPv4Token(token)
            if not self.isValidIPv4Token(token):
                return False
        return True
    
    def isValidIPv4Token(self, token):
        if len(token) > 3 or len(token) == 0:
            return False
        if token[0] == "0" and len(token) > 1:
            return False
        parsedInt = 0
        for i in range(len(token)):
            # print ord(token[i]) - ord("9")
            if 0 <= ord(token[i]) - ord("0") <= 9:
                parsedInt *= 10
                parsedInt += ord(token[i]) - ord("0")
                # print ord("9") - ord(token[i]), parsedInt
            else:
                return False
        # print "**************"
        # print parsedInt, token
        if parsedInt > 255:
            return False
        return True
    
    def isValidIPv6(self, IP):
        if len(IP) < 15:
            return False
        if IP[0] == ":":
            return False
        if IP[-1] == ":":
            return False
        tokens = IP.split(":")
        if len(tokens) != 8:
            return False
        for token in tokens:
            if not self.isValidIPv6Token(token):
                return False
        return True
    
    def isValidIPv6Token(self, token):
        if len(token) > 4 or len(token) == 0:
            return False
        for char in token:
            isDigit = 1 if 48 <= ord(char) <= 57 else 0
            isUpperCase = 1 if 65 <= ord(char) <= 70 else 0
            isLowerCase = 1 if 97 <= ord(char) <= 102 else 0
            if not (isDigit or isUpperCase or isLowerCase):
                return False
        return True
        
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.isValidIPv4(IP):
            return "IPv4"
        elif self.isValidIPv6(IP):
            return "IPv6"
        else:
            return "Neither"


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 3, 1, 1]
    print(countNums(nums))

    str = "()()()"
    print(validParenthese(str))

    IPSolution = Solution()
    ip = "172.16.254.1"
    print(IPSolution.validIPAddress(ip))

