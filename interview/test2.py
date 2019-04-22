#test
'''
import sys 
for line in sys.stdin:
    s = line.split()[0]
    dic = {}
    count = 0
    maxCount = 0
    i = 0
    while i < len(s):
        if s[i] not in dic:
            dic[s[i]] = 1
            count += 1
            i += 1
        else:
            maxCount = max(maxCount, count)
            count = 0
            dic = {}
    if maxCount == count == 0:
        print(1)
    print(max(maxCount,count))
'''
'''
import sys
def count(grid):
        check = set()
        def area(r,c):
            if not (0<=r<len(grid) and 0<=c<len(grid[0]) and (r, c) not in check and grid[r][c]):
                return 0
            check.add((r, c))
            return 1+area(r+1,c)+area(r-1,c)+area(r,c+1)+area(r,c-1)
        return len([1 for r in range(len(grid)) for c in range(len(grid[0])) if area(r,c) != 0])

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    matrix = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        for j in range(n):
            matrix[i][j] = values[j]
    print(count(matrix))
'''
'''
import sys
def dfs(user, graph, visited, n):
    if user in visited:
        return False
    visited.add(user)
    if len(visited) == n:
        return True
    followers = graph[user]
    return any([1 if dfs(follower, graph, visited, n) else 0 for follower in followers])

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    users = []
    relationships = []
    for i in range(2*M):
        if values[i] not in users:
            users.append(values[i])
        if i%2 == 0:
            A = values[i]
        else:
            B = values[i]
            relationships.append((A, B))

    G = {}
    for (A, B) in relationships:
        if B not in G:
            G[B] = set([A])
        else:
            G[B].add(A)

    count = 0
    for user in users:
        visited = set()
        if dfs(user, G, visited, N):
            count += 1
    print(count)
'''
'''
import sys

def isIpAddrLegal(ipStr):
    ip_split_list = ipStr.strip().split('.')
    if 4 != len(ip_split_list):
        return False
    for i in range(4):
        try:
            ip_split_list[i] = int(ip_split_list[i])
        except:
            return False
    for i in range(4):
        if ip_split_list[i] <= 255 and ip_split_list[i] >= 0:
            pass
        else:
            return False
    return True

for line in sys.stdin:
    s = line.split()[0]
    count = 0
    for i in range(len(s)-3):
        for j in range(i+1, len(s)-2):
            for k in range(j+1, len(s)-1):
                if isIpAddrLegal(s[:i+1]+'.'+s[i+1:j+1]+'.'+s[j+1:k+1]+'.'+s[k+1:]):
                    count += 1
    print(count)
'''
'''
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline().strip()))
    #a.sort()
    #sums = []
    for i in range(n):
        res = 0
        for j in range(n):
            if a[j] < a[i]:
                res += a[j]
            #else:
            #    break
        #sums.append(res)
        print(res)
'''
'''
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline().strip()))
    a.sort()
    count = 0
    for i in range(n):
        for j in range(i+1,n-1):
            if a[j] < a[j+1] < a[i]+18000:
                count += 1
            elif a[i]+18000 < a[j] < a[j+1]:
                count += 1
    print(count)

'''
'''
import sys
import os
import re



def  buildWall(n, m):
    #count = 0
    #matrix = [[None for _ in range(n)] for _ in range(m)]
    
    def dfs(i, j):
        if i == n-1 and j == m-1:
            return 1
        if 0<i<n and 0<j<m:
            return dfs(i,j+1)+dfs(i,j+2)+dfs(i,j+3)+dfs(i,j+4)+dfs(i+1,j+1)+dfs(i+1,j+2)+dfs(i+1,j+3)+dfs(i+1,j+4)
        else:
            return 0
    return dfs(0, 0)+dfs(0,1)+dfs(0,2)+dfs(0,3)


if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())

    for i in range(num):
        a = sys.stdin.readline().strip().split(' ')
        n = int(a[0])
        m = int(a[1])
        res = buildWall(n, m)
        print(str(res) + "\n")
'''
        
