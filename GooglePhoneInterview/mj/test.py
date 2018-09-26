'''
# time: O(nlogn)
def deletNode(root):
	if not root:
		return []
	resL = deletNode(root.left)
	resR = deletNode(root.right)
	if shouldBeDelete(root):
		root = None
		return resL + resR
	if root.left and root.left == resL[-1]:
		resL.pop()
	if root.right and root.right == resR[-1]:
		resR.pop()
	return (resL + resR).append(root)

# time: O(n)
def findSingle(l):
	res = l[0]
	for i in xrange(1, len(l)):
		res ^= l[i]
	return res

# time: O(logn)
def findSingle(l):
	l, r = 0, len(l) - 1
	while l <= r:
		mid = (l + r)/2
		if l[mid] != l[mid - 1] and l[mid] != l[mid + 1]:
			return l[mid]
		if l[mid] == l[mid - 1]:
			firstInd = mid - 1
		else:
			firstInd = mid
		if firstInd % 2 == 0:
			# single num in the right
			l = mid + 1
		else:
			# single num in the left
			r = mid - 1
'''
'''
def match(s, d):
	if len(s) != len(d):
		return False
	dic = {}
	# s[i], d[i]
	for s_i, d_i in zip(s, d):
		print s_i, d_i
		if s_i not in dic:
			dic[s_i] = d_i
		elif dic[s_i] != d_i:
			return False
	return True
'''
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    dic_s, dic_t = {}, {}
    for i, (s_i, t_i) in enumerate(zip(s, t)):
        if s_i not in dic_s:
            dic_s[s_i] = i
        if t_i not in dic_t:
            dic_t[t_i] = i
        if dic_s[s_i] != dic_t[t_i]:
            return False
    return True

if __name__ == "__main__":
	s = 'abba'
	d = 'cbbc'
	#print match(s, d)
	print isIsomorphic(s, d)




