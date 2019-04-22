# longest Increasing substring
class Solution(object):
    def lengthOfLIS(self, s):
        """
        :type s: str
        :rtype: str
        """
        # edge case
        # Time: O(n)
        # Space: O(n)
        if not s:
            return ""
        
        s_lowerCase = s.lower()
        res = ("", 0, 0)
        i = 0
        while i < len(s) - 1:
            if ord(s_lowerCase[i]) <= ord(s_lowerCase[i + 1]):
                # increasing subsequence starts
                j = i + 1
                while j < len(s):
                    if ord(s_lowerCase[j]) < ord(s_lowerCase[j - 1]):
                        break
                    j += 1
                j -= 1
                
                if res[2] - res[1] + 1 < j - i + 1:
                	res = (s[i : j + 1], i, j)
                
                i = j + 1
            else:
                i += 1
    
        return res[0]


# follow up
# 300 longest increasing subsequence
# https://www.youtube.com/watch?v=CE2b_-XfVDk
# Time: O(n * n)
# Space: O(n)
class Solution_followUp(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        i = 1
        
        while i < len(nums):
            j = 0
            currMax = dp[i]
            while j < i:
                if nums[j] < nums[i]:
                    currMax = max(currMax, dp[i] + dp[j])
                j += 1
            dp[i] = currMax
            i += 1
            # print dp
        return max(dp)
                
        
if __name__ == "__main__":
	str = "aAdbdcdEzxycg"
	sol = Solution()
	print(sol.lengthOfLIS(str))
