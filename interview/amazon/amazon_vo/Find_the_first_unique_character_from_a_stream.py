# Find the first non-repeating character from a stream of characters
# https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/

class Solution1(object):
    def __init__(self):
        """
        initialize your data structure
        """
        self.firstUnique = []
        self.hashset = set()

    def put(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.hashset:
            self.firstUnique.append(num)
            self.hashset.add(num)
        elif num in self.firstUnique:
            # O(n)
            self.firstUnique.remove(num)


    def getFirstUnique(self):
        """
        :rtype: int
        """
        if self.firstUnique:
            return self.firstUnique[0]
        else:
            return None


########################
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class Solution2(object):
    def __init__(self):
        """
        initialize your data structure
        """
        # double linkedlist
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

        # key: num value: node
        self.hashtable = {}

        # record appear
        self.hashset = set()

    def put(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.hashset:
            # add it into firstUnique linked list in the tail
            newNode = Node(num)

            newNode.next = self.tail
            newNode.prev = self.tail.prev

            newNode.next.prev = newNode
            newNode.prev.next = newNode

            self.hashtable[num] = newNode

            self.hashset.add(num)

        elif num in self.hashtable:
            # need to delete
            requiredNode = self.hashtable[num]
            requiredNode.prev.next = requiredNode.next
            requiredNode.next.prev = requiredNode.prev

            self.hashtable.pop(num)


    def getFirstUnique(self):
        """
        :rtype: int
        """
        if self.head.next:
            return self.head.next.val
        else:
            return None


if __name__ == "__main__":
    sol = Solution2()
    sol.put(1)
    print(sol.getFirstUnique())
    sol.put(2)
    print(sol.getFirstUnique())
    sol.put(1)
    print(sol.getFirstUnique())