#Image Matching
def imageMatching(map1, map2):
    resMatchNum = 0
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            region1 = bfsSearch(map1, i, j)
            region2 = bfsSearch(map2, i, j)
            if Match(region1,region2):
                resMatchNum += 1
    return resMatchNum

def bfsSearch(map, r, c):
    res = []
    if map[r][c]:
        queue = [(r,c)]
        while queue:
            coor = queue.pop(0)
            res.append(coor)
            r, c = coor
            map[r][c] = 0
            if r-1 >=0 and c<len(map[r-1]) and map[r-1][c]:
                queue.append((r-1,c))
            if r+1 <len(map) and c<len(map[r+1]) and map[r+1][c]:
                queue.append((r+1,c))
            if c-1 >=0 and map[r][c-1]:
                queue.append((r,c-1))
            if c+1 < len(map[r]) and map[r][c+1]:
                queue.append((r,c+1))
    return res
    
def Match(region1, region2):
    if len(region1) != len(region2) or not region1:
        return False
    for i in range(len(region1)):
        if region1[i] != region2[i]:
            return False
    return True

if __name__ == '__main__':
    # testcase1
    map1a = [[0,0,1],[0,1,1],[1,0,0]]
    map1b = [[0,0,1],[0,1,1],[1,0,1]]
    print(imageMatching(map1a, map1b))
    # 1

    # testcase2
    map2a = [[1,1,1],[1,0,0],[1,0,0]]
    map2b = [[1,1,1],[1,0,0],[1,0,1]]
    print(imageMatching(map2a, map2b))
    # 1
