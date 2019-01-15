# Count valid parenthesises number
def isValid(s):
	if not s:
		return True

	stack = []
	for char in s:
		if stack and ord(char) - ord(stack[-1]) == 1:
			stack.pop()
		else:
			stack.append(char)
	return not stack