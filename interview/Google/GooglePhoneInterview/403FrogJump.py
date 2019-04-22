# 403 Frog Jump
# idea comes from https://leetcode.com/problems/frog-jump/solution/
#https://www.youtube.com/watch?v=-FBfrVz841k
#https://leetcode.com/problems/frog-jump/discuss/88873/Python-DFS-easy-understanding-using-memo
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        '''
        #dp
        # idea is where is the last jump.
        # the important value is k in the current jump
        if not stones:
            return False
        
        hashset = {}
        #initial source of stones[0] and the rest of stones
        for i in range(len(stones)):
            hashset[stones[i]] = set()
        hashset[stones[0]].add(0) #source is 0 and unit in the first stone is 1 cz k+j > 0
        #print hashset
        
        for i in range(len(stones)):
            for k in hashset[stones[i]]:
                for j in [-1,0,1]:
                    # step = k+j
                    #print k+j
                    if k+j > 0 and stones[i]+k+j in hashset:
                        hashset[stones[i]+k+j].add(k+j)
                #print hashset
        return len(hashset[stones[-1]]) != 0
        '''
        # dfs with memo(meaning visited)
        def dfs(stones, current, speed, target):
            if (current, speed) in memo:
                return False
            if current == target:
                return True
            speeds = [speed-1, speed, speed+1]
            for s in speeds:
                if s > 0 and current+s in stones and dfs(stones, current+s, s, target):
                    return True
            memo.add((current, speed))
            return False
            
        memo = set()#memorry fall into the water
        lastStone = stones[-1]
        stones = set(stones)
        return dfs(stones, 0, 0, lastStone)
