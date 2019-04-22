'''
# abb --> aba
# abbb --> abcb
def change(s):
	if not s or len(s) <= 1:
		return 0
	f1, f2 = 0, 0
	for i in xrange(1, len(s)):
		if s[i] == s[i - 1]:
			f1, f2 = min(1 + f1, 1 + f2), f1
		print f1, f2
	return f1
'''
#################################################
'''
# global maximum
def permutation(l, m):

	def dfs(res, currList, l, m):
		if len(currList) == m:
			currList_ = sorted(currList)
			#print currList_
			minVal = float('inf')
			for i in range(1, len(currList_)):
				minVal = min(minVal, 
					abs(currList_[i] - currList_[i - 1]))
			#print minVal
			res.append(minVal)
		else:
			for i in range(len(l)):
				if l[i] not in currList:
					currList.append(l[i])
					dfs(res, currList, l, m)
					currList.pop()

	res = []
	if not l or len(l) == 0:
		return res.append(0)
	dfs(res, [], l, m)
	return max(res)
'''
##############################################
'''
def stringCompression(chars):
	ancher, write = 0, 0
	for read, char in enumerate(chars):
		if read + 1 == len(chars) or chars[read + 1] != char:
			chars[write] = chars[ancher]
			write += 1
			if read > ancher:
				for digit in str(read - ancher + 1):
					chars[write] = digit
					write += 1
			ancher = read + 1
	return write
'''
###############################################

# Given a positive integer target, count all the combinations of contiguous positive integers that sum up to the target.
# For Example,
# target = 15
# return 4

# since
# 15 = 4 + 5 + 6
# 15 = 1 + 2 + 3 + 4 + 5
# 15 = 7 + 8
# 15 = 15
'''
def consecutiveSum(N):
	resCount = 0
	k = 1
	while k * k <= 2 * N:
		if (2 * N) % k == 0:
			x = ((2 * N) / k - k - 1)
			if x % 2 == 0 and x >= 0:
				resCount += 1
		k += 1
	return resCount
'''
##################################################
'''
def num_PalindromicSubstring(s):
	if not s or len(s) == 0:
		return 0

	resCount = 0
	dp = [[False] * len(s) for _ in xrange(len(s))]
	record = set()

	for j in xrange(len(s)):
		for i in xrange(j + 1):
			dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
			if dp[i][j] and s[i:j + 1] not in record:
				resCount += 1
				record.add(s[i:j + 1])
				# print s[i:j + 1]
	return resCount
'''
####################################################
'''
def countBits(num):
	count = 0
	while num > 0:
		if (num & 1) > 0:
			count += 1
		num >>= 1
	return count

def insertionSort(arr, aux, n):
	# time: O(n * n)
	# space: O(n)
	print arr, aux
	for i in xrange(1, n):
		keyAux = aux[i]
		keyArr = arr[i]
		j = i - 1
		while j >= 0 and (aux[j] > keyAux or (aux[j] == keyAux and arr[j] > keyArr)):
			aux[j + 1] = aux[j]
			arr[j + 1] = arr[j]
			j -= 1
		aux[j + 1] = keyAux
		arr[j + 1] = keyArr

def dictInsertionSort(arr, aux, n):
	dic = {}
	for i, val in enumerate(aux):
		if val not in dic:
			dic[val] = [arr[i]]
		else:
			l = dic[val]
			done = False
			for j, compVal in enumerate(l):
				if arr[i] < compVal:
					l.insert(j, arr[i])
					done = True
					break
			if not done:
				l.append(arr[i])
			dic[val] = l
	res = []
	for key, val in sorted(dic.items(), key = lambda x: (x[0], x[1])):
		# print key, val
		res.extend(val)
	return res

def cardinalitySorting(arr):
	n = len(arr)
	aux = [None] * n
	for i in xrange(n):
		aux[i] = countBits(arr[i])

	# insertionSort(arr, aux, n)
	# return arr, aux

	res = dictInsertionSort(arr, aux, n)
	return res
'''
######################################################################
def str2num(i, s):
	num1 = 0
	factor = 10
	while 0 <= ord(s[i]) - ord('0') <= 9:
		num1 = num1 * factor + ord(s[i]) - ord('0')
		i += 1

	if s[i] == '.' and 0 <= ord(s[i + 1]) - ord('0') <= 9:
		i += 1
		num2 = 0
		factor = 0.1
		while 0 <= ord(s[i]) - ord('0') <= 9:
			num2 = num2 * factor + ord(s[i]) - ord('0')
			i += 1
		num1 = num1 + num2 * factor
	elif s[i] == '.' and not 0 <= ord(s[i + 1]) - ord('0') <= 9:
		i += 1
		return i, num1, False
	return i, num1, True


def isValid(s):
	# parenthesis check
	if s[0] != '(' or s[-1] != ')':
		return 'Invalid'
	
	i = 1
	X = True
	sign = 1
	while s[i] != ')':
		if s[i] == ' ':
			if s[i - 1] == ',':
				i += 1
				continue
			else:
				return 'Invalid'
		elif s[i] == ',':
			i += 1
			continue
		elif s[i] == '+':
			sign = 1
			i += 1
			continue
		elif s[i] == '-':
			sign = -1
			i += 1
			continue
		elif s[i] == '0':
			return 'Invalid'
		elif 0 < ord(s[i]) - ord('0') <= 9:
			i, val, validCheck = str2num(i, s)
			if not validCheck:
				return 'Invalid'
			if X:
				if -90.0 <= val <= 90.0:
					X = False
				else:
					return 'Invalid'
			else:
				if not -180.0 <= val <= 180.0:
					return 'Invalid'
			continue
		else:
			return 'Invalid'
	return 'valid'


if __name__ == "__main__":
	# s = 'abbbcc'
	# print change(s)

	# l = [1, 2, 3, 5, 7]
	# m = 4
	# print permutation(l, m)

	# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
	# print stringCompression(chars)

	# num = 15
	# print consecutiveSum(num)

	# s = "google"
	# print num_PalindromicSubstring(s)

	# inputList = [3, 5, 6, 1, 4, 2] #[1, 2, 3, 4]
	# print cardinalitySorting(inputList)

	# ss = ['(90, 180)', '(+90, +180)', ' (90, 180)', '(90.0, 180.1)', '(85S, 95W)', '(090, 180)']
	ss = ['(75, 180)', '(+90.0, -147.45)', '(77.11112223331, 149.99999999)', '(+90, +180)', '(90, 180)', '(-90.00000, -180.0000)', '(75, 280)', '(+190.0, -147.45)', '(77.11112223331, 249.99999999)', '(+90, +180.2)', '(90., 180.)', '(-090.00000, -180.0000)']
	for s in ss:
		print isValid(s)