# Rectangle Overlap
# Leetcode 836


# check position
# Time: O(1)
# Space: O(1)
class Solution1(object):
	def isRectangleOverlap(self, rec1, rec2):
		return not (rec1[2] <= rec2[0] or
			rec1[3] <= rec2[1] or
			rec1[0] >= rec2[2] or
			rec1[1] >= rec2[3])

# check Area intersect
# Time: O(1)
# Space: O(1)
class Solution2(object):
	def isRectangleOverlap(self, rec1, rec2):
		def intersect(p1, p2, q1, q2):
			return min(p2, q2) > max(p1, q1)

		return intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and intersect(rec1[1], rec1[3], rec2[1], rec2[3])
