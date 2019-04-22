# 844 Backspace string compare
# idea comes from: https://leetcode.com/problems/backspace-string-compare/solution/
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        '''
        # two stacks
        # TC: O(n)
        # SC: O(n)
        def string2stack(string):
            stack = []
            for i in range(len(string)):
                if string[i] != '#':
                    stack.append(string[i])
                elif stack:
                    stack.pop(-1)
            return stack
        return string2stack(S) == string2stack(T)
        '''
        '''
        # two pointers
        def pointer(string):
            pointer = 0
            while pointer < len(string):
                if string[pointer] == '#' and pointer != 0:
                    string = string[:pointer-1] + string[pointer+1:]
                    pointer -= 1
                    continue
                if string[pointer] == '#' and pointer == 0:
                    string = string[1:]
                    continue
                pointer += 1
            return string

        return pointer(S) == pointer(T)
        '''
        # skip
        # O(n), O(1)
        def F(S):
            skip = 0
            for char in reversed(S):
                if char == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield char
                    
        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
