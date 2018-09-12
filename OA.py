#OA
'''
import sys

a = sys.stdin.readline().strip().split('')
intervals.sort(key = lambda x : x.start()


import sys 
for line in sys.stdin:
    a = line.split()
    print int(a[0]) + int(a[1])

import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        for v in values:
            ans += v
    print ans
'''
import sys

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for t_ in range(t):
        n = int(sys.stdin.readline().strip())
        s = []
        for n_ in range(n):
            s.append(sys.stdin.readline().strip())
        if len(s) != 2:
            print('Problem!')
            continue
        if len(s[0]) != len(s[1]):
            print('Sad')
            continue
        # set s[0]
        i = 0
        temp = [i for i in s[1]]
        temp = ''.join(temp)
        while i < len(s[0]):
            if s[0] == temp:
                print('Yeah')
                break
            temp = temp[1:] + temp[0]
            i += 1
        if i == len(s[0]) and s[0] != temp:
            i = 0
            temp = [i for i in s[1][::-1]]
            temp = ''.join(temp)
            while i < len(s[0]):
                if s[0] == temp:
                    print('Yeah')
                    break
                temp = temp[1:] + temp[0]
                i += 1
        if i == len(s[0]) and s[0] != temp:
            print('Sad')
