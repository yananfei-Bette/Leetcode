# 4 Median of Two Sorted Anrrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # https://www.youtube.com/watch?v=do7ibYtv5nk
        # https://blog.csdn.net/chen_xinjia/article/details/69258706
        # time : O(log(min(m,n)))
        # space : O(1)
        ######################################
        #index 0   1   2   3   4   5
        
        #          L1   R1
        #nums1 3   5 |  8   9           4 cut1
        #nums2 1   2   7  | 10  11  12  6 cut2
        #              L2   R2
        
        
        #nums3 1  2  3  5  7 | 8  9  10  11  12
        
        #nums3 -> nums1 + nums2 -> nums1
        #######################################
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        l = len(nums1) + len(nums2)
        cut1 = 0
        cut2 = 0
        cutL = 0
        cutR = len(nums1)
        #while cut1 <= len(nums1):
        while cutL <= cutR:
            cut1 = (cutR + cutL) / 2
            cut2 = l / 2 - cut1
            #print cut1, cut2
            L1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            L2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            R1 = float('inf') if cut1 == len(nums1) else nums1[cut1]
            R2 = float('inf') if cut2 == len(nums2) else nums2[cut2]
            
            #print L1, R1
            #print L2, R2
            
            if L1 > R2:
                cutR = cut1 - 1
            elif L2 > R1:
                cutL = cut1 + 1
            else:
                if l % 2 == 0:
                    L1 = L1 if L1 > L2 else L2
                    R1 = R1 if R1 < R2 else R2
                    return (L1 + R1)*0.5
                else:
                    R1 = R1 if R1 < R2 else R2
                    return R1
        return  