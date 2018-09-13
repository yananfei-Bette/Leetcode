#useful code

#1
for day, flower in enumerate(flowers, 1):
    print(day, flower)

#2
sorted(dic.item(), key=lambda item: (item[1], item[0])
arr = sorted((value, key) for (key, value) in dic.items())

#3
arr[::-1]

#4
charInd = [i for i in range(len(s)) if s.startswith(char, i)]

#5
d = dict.fromkeys(words, 0)

#6
match_list = []
match_list += [i for x in range(d[min(d, key=d.get)])]

#7
import sys
t = int(sys.stdin.readline().strip())

#8
guess = random.choice(wordlist)

#9
wordlist = [word for word in wordlist if sum(i == j for i, j in zip(guess, word)) == n]

#10
count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if match(w1, w2) == 0)

#11
#create graph
G, W = collections.defaultdict(set), collections.defaultdict(float)
for (A, B), V in zip(equations, values):
    # set compute
    G[A], G[B] = G[A] | {B}, G[B] | {A}
    W[A, B], W[B, A] = V, 1.0/V

#12
#find the min length of A that B in A.
# reduced the problem to deciding whether B is a substring of some A * k
# the tricky part is the value of q
q = (len(B)-1)//len(A)+1

#13
# yield
# all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
        def F(S):
            skip = 0
            for char in reversed(S):
                if char == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield char
                    
        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))

#14
#initial a dictionary
def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        for i,val in enumerate(s):
            dic1[val] = dic1.get(val,[])+[i]
        for i,val in enumerate(t):
            dic2[val] = dic2.get(val,[])+[i]
        #print dic1,dic2
        #print sorted(dic1.values()), sorted(dic2.values())
        return sorted(dic1.values()) == sorted(dic2.values())

#15
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):

#16
workers = sorted((float(w)/q, q, w) for w, q in zip(wage, quality))

heapPool = []
#maxheap
heapq.heappush(heapPool, -q)
sumQualities += heapq.heappop(heapPool)

#17
#initialize a hash set
        hashset = {}
        #initial source of stones[0] and the rest of stones
        for i in range(len(stones)):
            hashset[stones[i]] = set()
        hashset[stones[0]].add(0) #source is 0 and unit in the first stone is 1 cz k+j > 0

#18
#dfs with memo(like visited)

#19 build binary tree
active = []
i = bisect.bisect(active, flower)

#20
class MedianFinder(object):
    #A max-heap to store the smaller half of the input numbers
    #A min-heap to store the larger half of the input numbers

    def __init__(self):
        """
        initialize your data structure here.
        """
        #maxheap
        self.lo = []
        #minheap
        self.hi = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lo) > len(self.hi):
            res = heapq.heappop(self.lo)
            heapq.heappush(self.lo, res)
            return float(-res)
        res_1 = heapq.heappop(self.lo)
        heapq.heappush(self.lo, res_1)
        res_2 = heapq.heappop(self.hi)
        heapq.heappush(self.hi, res_2)
        return (-res_1+res_2)*0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#21
''.join(str(r) for r in res)
