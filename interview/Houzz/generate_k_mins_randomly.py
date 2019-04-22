# generate k mins randomly
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=466106
class Solution1(object):
	def __init__(self):
		self.dic = set()

	def generate(self, m, n, k):
		import random
		random.seed(5)
		mines = random.sample(range(0, m * n), k)

		for mine in mines:
			x = mine // n
			y = mine % n
			self.dic.add((x, y))

	def checkMine(self, x, y):
		if (x, y) in self.dic:
			return True
		else:
			return False




# Resrvoir Sampling
"""
Reservoir sampling is a family of randomized algorithms for 
randomly choosing k samples from a list of n items, 
where n is either a very large or unknown number. 

Typically n is large enough that the list doesn’t fit into main memory. 
"""
# An efficient Python3 program  
# to randomly select k items 
# from a stream of items 
import random 
# A utility function  
# to print an array 
def printArray(stream,n): 
    for i in range(n): 
        print(stream[i],end=" "); 
    print(); 
  
# A function to randomly select 
# k items from stream[0..n-1]. 
def selectKItems(stream, n, k): 
        i=0;  
        # index for elements 
        # in stream[] 
          
        # reservoir[] is the output  
        # array. Initialize it with 
        # first k elements from stream[] 
        reservoir = [0]*k; 
        for i in range(k): 
            reservoir[i] = stream[i]; 
          
        # Iterate from the (k+1)th 
        # element to nth element 
        while(i < n): 
            # Pick a random index 
            # from 0 to i. 
            j = random.randrange(i+1); 
              
            # If the randomly picked 
            # index is smaller than k, 
            # then replace the element 
            # present at the index 
            # with new element from stream 
            if(j < k): 
                reservoir[j] = stream[i]; 
            i+=1; 
          
        print("Following are k randomly selected items"); 
        printArray(reservoir, k); 
      
# Driver Code 
  
if __name__ == "__main__": 
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 
    n = len(stream); 
    k = 5; 
    selectKItems(stream, n, k); 
  
# This code is contributed by mits 






if __name__ == "__main__":
	m = 5
	n = 6
	k = 4
	sol = Solution()
	sol.generate(m, n, k)
	print(sol.checkMine(3, 1))
	print(sol.checkMine(0, 0))