# 3 Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # my method
        '''
        dic = {}
        maxCount = 0
        count = 0
        i = 0
        while i < len(s):
            if s[i] not in dic:
                dic[s[i]] = i
                count += 1
                i += 1
            else:
                maxCount = max(maxCount, count)
                i = dic[s[i]] + 1
                dic = {}
                count = 0
        return max(maxCount, count)
        '''
        #############################
        # sliding widow using hashset with two pointers
        '''
        n = len(s)
        i, j = 0, 0
        hashset = set()
        maxCount = 0
        while i < n and j < n:
            if s[j] not in hashset:
                hashset.add(s[j])
                j += 1
                maxCount = max(maxCount, j - i)
            else:
                hashset.remove(s[i])
                i += 1
        return maxCount
        '''
        ################################
        # my idea improvement. no need to create the new dic
        '''
        n = len(s)
        i, j = 0, 0
        dic = {}
        maxCount = 0
        while j < n:
            if s[j] in dic:    
                i = max(dic[s[j]], i)
            maxCount = max(maxCount, j - i + 1)
            dic[s[j]] = j + 1
            j += 1
        return maxCount
        '''
        # use list instead of hashmap
        n = len(s)
        maxCount = 0
        index = [0] * 128
        i, j = 0, 0
        while j < n:
            i = max(index[ord(s[j])], i)
            maxCount = max(maxCount, j - i + 1)
            index[ord(s[j])] = j + 1
            j += 1
        return maxCount
        
        

if __name__ == "__main__":
	s = " "
	print lengthOfLongestSubstring(s)