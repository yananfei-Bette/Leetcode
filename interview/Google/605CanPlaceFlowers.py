#605 Can Place Flowers
# Greed
# idea comes from https://mp.weixin.qq.com/s?__biz=MzA5MzE4MjgyMw==&mid=2649458229&idx=1&sn=2861d46c0f651e2efe9353c3d94dec35&scene=21#wechat_redirect
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                count += 1
                flowerbed[i] = 1
            if count >= n:
                return True
        return False
