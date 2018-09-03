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
