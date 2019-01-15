# nvidia oa
def arrange(avgL, deltas, remain):
	# print deltas
	if avgL % 2 == 0:
		i = 0
		while remain > 1 and i < len(deltas):
			deltas[i] += 2
			remain -= 2
			i += 1
		if remain == 1 and i < len(deltas):
			deltas[i] += 1
			remain -= 1
		if remain:
			avgL += 2
	else:
		i = 0
		while remain and i < len(deltas):
			deltas[i] += 1
			remain -= 1
			i += 1
		if remain:
			avgL += 1
	return avgL, deltas, remain

def split(str, num):
	# split str into given number of substring
	# the length of substring should be as even as possible
	# lengths of each substring should be in descending order
	# However, order of each character should be maintain as the orignial order, so that we can easily retrieve back.
	# Minimize the maximum length different.
	# example
	# str: abcdefg
	# num: 2
	# result: abcd, efg
	# input type: str, int
	# output type: list[str]
	if not str or len(str) < num:
		return ['']
	if len(str) == num:
		return list(str)

	avgL = len(str) / num
	if len(str) % num == 0:
		res = []
		for i in xrange(0, len(str), avgL):
			res.append(str[i:i+avgL])
		return res

	deltas = [avgL] * num
	remain = len(str) % num
	while remain:
		# print deltas
		avgL, deltas, remain = arrange(avgL, deltas, remain)

	i = 0
	j = 0
	res = []
	while i < len(str) and j < len(deltas):
		res.append(str[i: i + deltas[j]])
		i += deltas[j]
		j += 1
	return res

if __name__ == "__main__":
	str = "abcdefghijklmn"
	num = 5
	print split(str, num)
