# 677 Map Sum Pairs
# Trie

class TrieNode(object):
    def __init__(self):
        #self.prefix = ''
        self.score = 0
        self.children = {}

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        '''
        # method 1 simple hashmap
        # time : O(N*P)
        self.hashmap = {}
        '''
        
        '''
        # method 2 prefix hashmap
        # store prefix score
        # time O(K)
        self.hashmap = {}
        self.scores = {}
        '''
        
        # method 3 Trie
        # time O(K)
        self.hashmap = {}
        self.root = TrieNode()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        '''
        # method 1
        self.hashmap[key] = val
        '''
        
        '''
        # method 2
        delta = val - self.hashmap.get(key, 0)
        self.hashmap[key] = val
        for i in range(1, len(key) + 1):
            prefix = key[:i]
            self.scores[prefix] = self.scores.get(prefix, 0) + delta
        '''
        
        # method 3
        delta = val - self.hashmap.get(key, 0)
        self.hashmap[key] = val
        curr = self.root
        curr.score += delta
        for char in key:
            curr = curr.children.setdefault(char, TrieNode())
            curr.score += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        '''
        # method 1
        return sum(val for key, val in self.hashmap.items() if key.startswith(prefix))
        '''
        
        '''
        # method 2
        #print self.scores
        return self.scores[prefix] if prefix in self.scores else 0
        '''
        
        # method 3
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.score
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)