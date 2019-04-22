# 683 K Empty Slots
'''
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn’t such day, output -1.

e.g. 1
input: flowers = [1,3,2]
       k =1
output:2

e.g. 2
input :flowers = [1,2,3]
       k = 1
output: -1
'''
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        '''
        # brute force Time Limit Exceeded
        # TC: O(nk)
        # SP: O(n)
        
        n = len(flowers)
        if n == 0 or k >= n:
            return -1
        check = [0]*(n+1)
        #######
        def IsValid(x, k, n, check):
            check[x] = 1
            if x+k+1<=n and check[x+k+1]:
                valid = True
                for j in range(1,k+1):
                    if check[x+j]:
                        valid = False
                        break
                if valid:
                    return True
                
            if x-k-1>=0 and check[x-k-1]:
                for j in range(1,k+1):
                    if check[x-j]:
                        return False
                return True
            
            return False
        ########
                        
        for i in range(n):
            if IsValid(flowers[i], k, n, check):
                return i+1
        return -1
        '''


        # BST tree
        # TC: O(nlogn)
        # SC: O(n)
        active = []
        for day, flower in enumerate(flowers, 1):
            i = bisect.bisect(active, flower)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1
