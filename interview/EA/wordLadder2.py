# wordLadder2

class Solution1(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # backtrack
        # find all possible solutions
        def backtrack(endWord, wordDic, curr):
            if curr[-1] == endWord:
                if not self.res:
                    self.res.append([char for char in curr])
                else:
                    l = len(self.res[0])
                    currL = len(curr)
                    if currL == l:
                        self.res.append([char for char in curr])
                    elif currL < l:
                        self.res = [[char for char in curr]]
                return
            
            if not wordDic:
                return
            
            word = curr[-1]
            for i in range(len(word)):
                for j in range(26):
                    temp = list(word)
                    temp[i] = chr(ord('a') + j)
                    candidate = ''.join(temp)
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


class Solution2(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # bfs
        # reduce time complexity
        # use bfs to check if we have result or not
        # while build a possible graph
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
                        candidate = ''.join(temp)
                        if candidate == endWord:
                            found = True

                        if candidate in wordDic:
                            if candidate not in nextLevel:
                                nextLevel.append(candidate)
                                visited.add(candidate)

                            # build graph
                            graph[candidate] = graph.get(candidate, []) + [word]
            queue = nextLevel
            wordDic -= visited
            
            if found:
                break
        
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
                        
                    
            
        
        
        
        
 
