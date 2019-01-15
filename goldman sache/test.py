#!/bin/python

import math
import os
import random
import re
import sys



# Complete the MinSliceWeight function below.
def MinSliceWeight(Matrix):
    '''
    # print Matrix
    N = len(Matrix)
    minRes = float("inf")
    if N == 0:
        return minRes

    #####################
    def helper(Matrix, startCol, currRow, currCol, currCount, currMin):
    # print minRes, startCol, currRow, currCol, currCount
        if currRow == len(Matrix) - 1:
            currMin = min(currMin, currCount + Matrix[currRow][currCol])
            # print(currMin)
            return currMin

        for nextCol in [currCol - 1, currCol, currCol + 1]:
            if 0 <= nextCol < len(Matrix) and abs(startCol - nextCol) < 2:
                currMin = helper(Matrix, startCol, currRow + 1, nextCol, currCount + Matrix[currRow][currCol], currMin)
        return currMin
    ######################
       
    for i in range(N):
        minRes = min(minRes, helper(Matrix, i, 0, i, 0, float("inf")))
    return minRes
    '''
    N = len(Matrix)
    if N == 0:
        return 0
    # Initialize cost table
    dp = [[float("inf")] * N for i in range(N)]
    for col in range(N):
        dp[0][col] = Matrix[0][col]

    # Run dynamic program
    for row in range(1, N):
        for col in range(N):
            currMin = float("inf")
            for previousCol in [col - 1, col, col + 1]:
                if 0 <= previousCol < N:
                    currMin = min(currMin, dp[row - 1][previousCol])
            dp[row][col] = Matrix[row][col] + currMin
    res = float("inf")
    for i in range(N):
        res = min(res, dp[N - 1][i])
    return res

if __name__ == '__main__':