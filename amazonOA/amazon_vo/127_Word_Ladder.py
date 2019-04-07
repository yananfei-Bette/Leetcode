# 127 Word Ladder

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # general idea
        # its a graph, can use BFS to solve
        # Time: O(m * n)
        # Space: O(m * n)

        wordDic = set(wordList)
        wordDic.discard(beginWord)
        if endWord not in wordDic:
            return 0

        queue = [beginWord]
        level = 1

        while queue:
            nextLevel = []

            for word in queue:
                if word == endWord:
                    return level

                for i in range(len(word)):
                    for j in range(26):
                        temp = list(word)
                        temp[i] = chr(ord('a') + j)
                        candidate = "".join(temp)

                        if candidate in wordDic:
                            nextLevel.append(candidate)
                            wordDic.discard(candidate)

            queue = nextLevel
            level += 1

        return 0


# follow up
# 126 word ladder ii

# backtrack --> recursion, dfs
class Solution_followUp(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def backtrack(endWord, wordDic, curr):
            if curr[-1] == endWord:
                if not self.res or len(self.res[0]) == len(curr):
                    self.res.append([e for e in curr])
                elif len(self.res[0]) > len(curr):
                    self.res = [[e for e  in curr]]
                return

            if not wordDic:
                return

            word = curr[-1]
            for i in range(len(word)):
                for j in range(26):
                    temp = list(word)
                    temp[i] = chr(ord('a') + j)
                    candidate = "".join(temp)

                    if candidate in wordDic:
                        wordDic.discard(candidate)
                        backtrack(endWord, wordDic, curr + [candidate])
                        wordDic.add(candidate)
            return

        wordDic = set(wordList)
        wordDic.discard(beginWord)
        if endWord not in wordDic:
            return []

        self.res = []
        backtrack(endWord, wordDic, [beginWord])
        return self.res


# bfs
# reduce time complexity
# use bfs to check if we have result or not
# while build a possible graph
# then use dfs to find the path
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordDic = set(wordList)
        wordDic.discard(beginWord)
        if endWord not in wordDic:
            return []

        found = False
        graph = {}
        queue = [beginWord]

        while queue:
            nextLevel = []
            visited = set()

            for word in queue:
                for i in range(len(word)):
                    for j in range(26):
                        temp = list(word)
                        temp[i] = chr(ord('a') + j)
                        candidate = "".join(temp)

                        if candidate == endWord:
                            found = True

                        if candidate in wordDic:
                            if candidate not in visited:
                                nextLevel.append(candidate)
                                visited.add(candidate)

                            # build graph
                            graph[candidate] = graph.get(candidate, []) + [word]

            if found:
                break

            queue = nextLevel
            wordDic -= visited

        if not found:
            return []

        res = []

        def dfs(graph, word, beginWord, res, curr):
            if word == beginWord:
                res.append([word] + curr)
                return

            for parent in graph[word]:
                dfs(graph, parent, beginWord, res, [word] + curr)
            return

        dfs(graph, endWord, beginWord, res, [])
        return res


