# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=491260

# calculator
# leetcode 224

class Solution1(object):
	def calculate(self, s):
		# stack
		# time: O(n)
		stack = []
		res = 0
		sign = 1
		i = 0
		while i < len(s):
			# number
			if 0 <= ord(s[i]) - ord('0') <= 9:
				num = ord(s[i]) - ord('0')
				while i + 1 < len(s) and 0 <= ord(s[i + 1]) - ord('0') <= 9:
					num = num * 10 + ord(s[i + 1]) - ord('0')
					i += 1

				res += num * sign

			# +
			elif s[i] == "+":
				sign = 1
			elif s[i] == '-':
				sign = -1
			elif s[i] == "(":
				stack.append(res)
				stack.append(sign)
				res = 0
				sign = 1
			elif s[i] == ")":
				res = res * stack.pop() + stack.pop()
			i += 1

		return res





# calculator II
# leetcode 227
class Solution2(object):
	def calculate(self, s):
		if not s:
			return 0

		stack = []
		num = 0
		sign = "+"

		for i in range(len(s)):
			if 0 <= ord(s[i]) - ord('0') <= 9:
				num = num * 10 + ord(s[i]) - ord('0')

			if (not 0 <= ord(s[i]) - ord('0') <= 9 and s[i] != " ") or i == len(s) - 1:
				if sign == "+":
					stack.append(num)
				elif sign == "-":
					stack.append(-num)
				elif sign == "*":
					stack.append(stack.pop() * num)
				else:
					temp = stack.pop()
					if temp / num < 0 and temp % num != 0:
						stack.append(temp / num + 1)
					else:
						stack.append(temp / num)
				sign = s[i]
				num = 0
		return sum(stack)





# Different ways to add parentheses
# leetcode 241
class Solution3(object):
	def diffWayToCompute(self, input):
		if input.isdigit():
			return [int(input)]

		res = []
		for i in range(len(input)):
			if input[i] in {'+', '-', '*'}:
				leftRes = self.diffWayToCompute(input[: i])
				rightRes = self.diffWayToCompute(input[i + 1:])

				for l in leftRes:
					for r in rightRes:
						res.append(self.operator(l, r, input[i]))
		return res

	def operator(self, num1, num2, operator):
		if operator == '+':
			return num1 + num2
		if operator == '-':
			return num1 - num2
		if operator == '*':
			return num1 * num2
		else:
			return None





# Expression add operators
# leetcode 282
class Solution4(object):
	def addOperators(self, num, target):
		"""
		:type num: str
		:type target: int
		:rtype: List[str]
		"""
		N = len(num)
		res = []

		###############
		def backtrack(index, prevOperand, currOperand, value, string):
			if index == N:
				if value == target and currOperand == 0:
					res.append("".join(string[1:]))
				return

			# expand currOperand with one char
			currOperand = currOperand * 10 + int(num[index])
			strCurrOperand = str(currOperand)

			# in case 05, as we know it's invalid
			# do nothing, just expand operand
			if currOperand > 0:
				backtrack(index + 1, prevOperand, currOperand, value, string)

			# Add
			string.append("+")
			string.append(strCurrOperand)
			backtrack(index + 1, currOperand, 0, value + currOperand, string)
			string.pop()
			string.pop()

			# next string must has one value
			if string:
				# subtract
				string.append("-")
				string.append(strCurrOperand)
				backtrack(index + 1, -currOperand, 0, value - currOperand, string)
				string.pop()
				string.pop()


				# Multiply
				string.append("*")
				string.append(strCurrOperand)
				backtrack(index + 1, currOperand * prevOperand, 0, value - prevOperand + currOperand * prevOperand, string)
				string.pop()
				string.pop()

			return
		###############

		backtrack(0, 0, 0, 0, [])
		return res





# calculator III
# leetcode 772
# https://leetcode.com/problems/basic-calculator-iii/discuss/113600/Java-and-Python-O(n)-Solution-Using-Two-Stacks

class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# first define a couple helper methods
		# operation helper to perform basic math operations
		def operation(op, second, first):
			if op == "+":
				return first + second
			elif op == "-":
				return first - second
			elif op == "*":
				return first * second
			elif op == "/":  # integer division
				return first // second
		
		# calculate the relative precedence of the the operators "()" > "*/" > "+="
		# and determine if we want to do a pre-calculation in the stack
		# (when current_op is <= op_from_ops)
		def precedence(current_op, op_from_ops):
			if op_from_ops in {"(", ")"}:
				return False
			if current_op in {"*", "/"} and op_from_ops in {"+", "-"}:
				return False
			return True
		
		if not s:
			return 0
		# define two stack: nums to store the numbers and ops to store the operators
		nums, ops = [], []
		i = 0
		while i < len(s):
			c = s[i]
			if c == " ":
				i += 1
				continue
			elif c.isdigit():
				num = int(c)
				while i < len(s) - 1 and s[i + 1].isdigit():
					num = num * 10 + int(s[i + 1])
					i += 1
				nums.append(num)
			elif c == "(":
				ops.append(c)
			elif c == ")":
				# do the math when we encounter a ')' until '('
				while ops[-1] != "(":
					nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
				ops.pop()
			elif c in {"+", "-", "*", "/"}:
				while len(ops) != 0 and precedence(c, ops[-1]):
					nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
				ops.append(c)
			i += 1
			
		while len(ops) > 0:
			nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
		
		return nums.pop()













