# 381 Insert Delete GetRandom O(1)
# hashmap + list
# hashmap with set

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.arr = []
        self.arr_len = 0
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.arr.append(val)
        self.arr_len += 1
        if val not in self.dic:
            self.dic[val] = {self.arr_len - 1}
            return True
        self.dic[val].add(self.arr_len - 1)
        return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        ind = self.dic[val].pop()
        last = self.arr[-1]
        self.arr[ind] = last
        self.dic[last].add(ind)
        self.dic[last].remove(self.arr_len - 1)
            
        if not self.dic[val]:
            del self.dic[val]
            
        self.arr.pop()
        self.arr_len -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        ind = random.randint(0, self.arr_len - 1)
        return self.arr[ind]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()