# 380 Insert Delete GetRandom O(1)
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.arr = []
        self.arr_len = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.arr.append(val)
        self.arr_len += 1
        self.dic[val] = self.arr_len - 1        
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        ind = self.dic[val]
        lastVal = self.arr[-1]
        self.arr[ind] = lastVal
        self.dic[lastVal] = ind
        del self.dic[val]
        self.arr.pop()
        self.arr_len -= 1
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        ind = random.randint(0, self.arr_len - 1)
        return self.arr[ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()