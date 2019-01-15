# Remove vowels
# Given a string, remove the vowels form the string and print the string without vowels
# e.g.
# Input: welcome to geeksforgeeks
# Output: wlcm t gksfrgks
# https://www.geeksforgeeks.org/program-remove-vowels-string/

def removeVowels(string):
	res = ""
	dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	for char in string:
		if char in dic:
			continue
		res += char
	return res