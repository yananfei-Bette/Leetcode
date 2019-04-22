# 232 Implement Queue using Stacks
"""
Queue is FIFO (first in - first out) data structure, 
in which the elements are inserted from one side - rear 
and removed from the other - front. 

The most intuitive way to implement it is with linked lists, 
but this article will introduce another approach using stacks. 

Stack is LIFO (last in - first out) data structure, 
in which elements are added and removed from the same end, called top. 

To satisfy FIFO property of a queue we need to keep two stacks. 
They serve to reverse arrival order of the elements and 
one of them store the queue elements in their final order.
"""

# Two stacks
# Push - O(1)
# Pop - O(1)
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = []
        self.back = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.back.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.front:
            return self.front.pop()
        else:
            while self.back:
                self.front.append(self.back.pop())

            if self.front:
                return self.front.pop()
            else:
                return None
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.front:
            return self.front[-1]
        else:
            while self.back:
                self.front.append(self.back.pop())

            if self.front:
                return self.front[-1]
            else:
                return None
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.front and not self.back:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()