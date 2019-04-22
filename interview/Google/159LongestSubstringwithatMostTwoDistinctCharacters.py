#159 Longest Substring with at Most Two Distinct Characters
#idea link: https://www.youtube.com/watch?v=Q1QInMLGpj4

#two pointers
#i = maxLen = 0
#i points the begining of window
#s[j] != s[k]
#k pass through s
#TC:O(n)
#SC:O(1)
def lengthOfLongestSubstringTwoDistinct_2pointers(s):
    i, maxLen = 0, 0
    j = -1
    for k in range(1, len(s)):
        if s[k] == s[k-1]:
            continue
        if j >= 0 and s[k]!=s[j]:
            maxLen = max(maxLen, k-i)
            #print(k, maxLen)
            i = j+1
        j = k-1
    return max(maxLen, len(s)-i)

#hash table
#satisfied k different characters
#TC:O(n)
#SC:O(1)
def lengthOfLongestSubstringTwoDistinct_hashTable(s):
    counts = [0]*256 #assume ASCII code
    i, maxLen, numDiff = 0, 0, 0
    for k in range(len(s)):
        if counts[ord(s[k])] == 0:
            numDiff += 1
        counts[ord(s[k])] += 1
        while i < len(s) and numDiff > 2:
            counts[ord(s[i])] -= 1
            if counts[ord(s[i])] == 0:
                numDiff -= 1
            i += 1
        maxLen = max(maxLen, k-i+1)
    return maxLen

if __name__ == "__main__":
    #s = "eecebaaaaa"
    s = '121343512'
    print('********result 1: two pointers********')
    print(lengthOfLongestSubstringTwoDistinct_2pointers(s))
    print('********result 2: hash table**********')
    print(lengthOfLongestSubstringTwoDistinct_hashTable(s))
