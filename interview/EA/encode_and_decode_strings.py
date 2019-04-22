# encode and decode strings
# leetcode 271

class Codec:

	def encode(self, strs):
		"""Encodes a list of strings to a single string.
		
		:type strs: List[str]
		:rtype: str
		"""
		res = ""
		for s in strs:
			res += str(len(s)) + "#" + s
		return res
		

	def decode(self, s):
		"""Decodes a single string to a list of strings.
		
		:type s: str
		:rtype: List[str]
		"""
		res, i = [], 0
		while i < len(s):
			ind = s[i:].find("#")
			size = int(s[i: i + ind])
			res.append(s[i + ind + 1: i + ind + 1 + size])
			i += ind + size + 1
		return res
		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))