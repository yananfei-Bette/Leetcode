# most people

import heapq

def most_people(intervals):
    if not intervals:
        return 0
    intervals.sort(key = lambda x: x[0])
    minheap = []
    for interval in intervals:
        if minheap and minheap[0] <= interval[1]:
            heapq.heappop(minheap)
        heapq.heappush(minheap, interval[0])
    return len(minheap)

# two sum, three sum
# merge two sorted array
# unique
# LRU
# number of island
# topology


#############################

# Design a ListNode, which has add() and search() functions
# search time O(1)
# LRU

# ask, duplicate
# ask function get, and return type

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

class Solution1(object):
    def __init__(self):
        self.hashmap = {}
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, x):
        # add into the tail
        # if we don't consider duplicate
        newNode = ListNode(x)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        newNode.prev.next = newNode
        newNode.next.prev = newNode

        self.hashmap[x] = newNode

    def search(self, x):
        if x in self.hashmap:
            return self.hashmap[x]
        else:
            None

#####################################
# 2 sum with duplicate
# [3,3,3]k=6, res = [0,0],[0,1],[0,2]....[2,0],[2,1],[2,2], total = 9
# Time: O(n)
# Space: O(n)
class Solution2(object):
    def twoSum_duplicate(self, nums, k):
        """
        type: nums: List[int]
        type: k: int
        rtypr: int
        """
        # edge case
        if not nums:
            return 0

        # use hashmap to count
        count = {}
        for i, val in enumerate(nums):
            count[val] = count.get(val, []) + [i]

        res = 0
        for i, val in enumerate(nums):
            x = k - val
            if x in count:
                res += len(count[x])
        return res


######################################
# Time: O(nlogn)
# Space: O(1) if we use in-place sort, quick sort
# binary search
# two times to find two boundary

# ask requirements
# clearify

class Solution3(object):
    def twoSum_duplicate(self, nums, k):
        """
        type: nums: List[int]
        type: k: int
        rtypr: int
        """
        # edge case
        if not nums:
            return 0

        nums.sort()
        res = 0

        def findSecond(num1, ind):
            res = 0
            if ind < len(nums):
                # get start of target number
                l, r = ind, len(nums) - 1
                startInd = -1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] + num1 > k:
                        r = mid - 1
                    elif nums[mid] + num1 == k:
                        startInd = mid
                        r = mid - 1
                    else:
                        l = mid + 1

                # get end index of target number
                l, r = ind, len(nums) - 1
                endInd = -1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] + num1 > k:
                        r = mid - 1
                    elif nums[mid] + num1 == k:
                        endInd = mid
                        l = mid + 1
                    else:
                        l = mid + 1

                # count
                res = endInd - startInd + 1
            return res

        for i in range(len(nums)):
            num1 = nums[i]
            currRes = findSecond(num1, 0)
            if currRes > 0:
                res += currRes
        return res


#############################
# word Ladder
class Solution4(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # BFS
        # Time: O(m * n)
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

########################
# path sum
class Solution5(object):
    def minPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None

        self.res = float("inf")

        def dfs(node, currSum):
            if not node:
                return
            if not node.left and not node.right:
                self.res = min(self.res, currSum)
                return

            if node.left:
                dfs(node.left, currSum + node.left.val)
            if node.right:
                dfs(node.right, currSum + node.right.val)
            return

        dfs(root, root.val)
        return self.res


# path sum
# print path
class Solution5(object):
    def minPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None

        self.res = [(float("inf"), [])]

        def dfs(node, currSum, currPath):
            if not node:
                return
            if not node.left and not node.right:
                if currSum < self.res[0][0]:
                    self.res = [(currSum, currPath)]
                elif currSum == self.res[0][0]:
                    self.res.append((currSum, currPath))
                return

            if node.left:
                dfs(node.left, currSum + node.left.val, currPath + [node.left.val])
            if node.right:
                dfs(node.right, currSum + node.right.val, currPath + [node.right.val])
            return

        dfs(root, root.val, [root.val])
        return self.res[0][1] if self.res[0][0] != float("inf") else []

###########
# path sum iii
class Solution6(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # edge case
        if not root:
            return 0

        return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def findPath(self, root, sum):
        if not root:
            return 0
        sum -= root.val
        res = 1 if sum == 0 else 0
        return res + self.findPath(root.left, sum) + self.findPath(root.right, sum)

##########
class Solution7(object):
    def __init__(self):
        self.available = []
        self.currReach = 1

    def checkout(self):
        if not self.available:
            res = None
            if self.currReach < 2 ** 64:
                res = self.currReach
                self.currReach += 1
            return res
        else:
            if self.available[0] < self.currReach:
                return heapq.heappop(self.available)
            else:
                res = None
                if self.currReach < 2 ** 64:
                    res = self.currReach
                    self.currReach += 1
                return res


    def checkin(self, num):
        heapq.heappush(self.available, num)



###########################
# sum of subtree
class Solution8(object):
    # Time: O(n)
    # Space: O(n)
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # edge case
        if not root:
            return []

        count = {}
        def helper(node):
            if not node:
                return 0
            res = node.val + helper(node.left) + helper(node.right)
            count[res] = count.get(res, 0) + 1
            return res
            
        helper(root)

        res = []
        maxCount = None
        for key, val in sorted(count.items(), key = lambda x: x[1], reverse = True):
            if maxCount == None or maxCount == val:
                res.append(key)
            else:
                break
        return res

##########################
# pow(a, b)
class Solution9(object):
    # Brute force
    def myPow1(self, a, b):
        # edge case
        # Time: O(b)
        # Space: O(1)
        if a == 0:
            return 0
        if b == 0:
            return 1

        def helper(a, b):
            res = 1
            for i in range(1, b + 1):
                res *= x
            return res

        sign = 1
        if b < 0:
            sign = 0
        return helper(a, b) if sign else 1.0 / helper(a, -b)

    # improve
    # recursion
    # Time: O(logb)
    # Space: O(1)
    def myPow2(self, a, b):
        # edge case
        if a == 0:
            return 0
        if b == 0:
            return 1

        def helper(a, b):
            if b == 0:
                return 1
            res = helper(a, b // 2)
            if b % 2:
                return res * res
            else:
                return res * res * a

        sign = 1
        if b < 0:
            sign = 0
        return helper(a, b) if sign else 1.0 / helper(a, -b)

    # Iteration
    # Time: O(logn)
    # Space: O(1)
    def myPow3(self, a, b):
        # edge case
        if a == 0:
            return 0
        if b == 0:
            return 1

        sign = 1
        if b < 0:
            sign = 0

        res = 1
        curr = a
        i = n

        while i > 0:
            if i % 2 == 1:
                res *= curr
            curr *= curr
            i /= 2

        return res if sign else 1.0 / res


##########
# leetcode 28 strStr()
class Solution10(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # edge case
        # ask
        if not haystack and not needle:
            return 0
        if not haystack:
            return -1
        if not needle:
            return 0

        i = 0
        while True:
            j = 0
            while True:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return - 1
                if needle[j] != haystack[i + j]:
                    break
                j += 1
            i += 1
        return -1


##############
# leetcode 387 find first unique char in string
class Solution11(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case
        # ask
        if not s:
            return -1

        count = {}
        for i, char in enumerate(s):
            count[char] = count.get(char, []) + [i]

        res = []
        for val in count.values():
            if len(val) == 1:
                res.extend(val)

        res.sort()
        return res[0] if res else -1


##############
# check string
class Solution12(object):
    def checkString(self, boxes, target):
        """
        :type s: str
        :rtype: int
        """
        # edge case discuss
        # duplicate or not
        # if don't have boxes
        # if we dont have target

        dic = {}
        for i, val in enumerate(boxes):
            if val:
                temp = {}
                for v in val:
                    temp[v] = temp.get(v, 0) + 1
                dic[i] = temp
            else:
                continue

        # print(dic)

        i = 0
        while i < len(target):
            mark_i = i
            char = target[i]
            for temp in dic.values():
                if char in temp and temp[char] > 0:
                    temp[char] -= 1
                    i += 1
                    break
            if mark_i == i:
                return False
        return True





if __name__ == "__main__":
    '''
    nums = [3, 3, 3]
    k = 6
    sol = Solution2()
    print(sol.twoSum_duplicate(nums, k))
    '''
    '''
    sol = Solution7()
    print(sol.checkout())
    print(sol.checkout())
    print(sol.checkout())
    print(sol.checkin(2))
    print(sol.checkout())
    print(sol.checkout())
    '''
    boxes = [['a', 'b'], ['a', 'c'], ['a', 'd']]
    target = "aac"
    sol = Solution12()
    print(sol.checkString(boxes, target))







