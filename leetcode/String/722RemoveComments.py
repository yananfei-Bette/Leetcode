#722 Remove Comments
# idea comes from https://leetcode.com/problems/remove-comments/solution/
'''
Intuition and Algorithm

We need to parse the source line by line. Our state is that we either are in a block comment or not.

If we start a block comment and we aren't in a block, then we will skip over the next two characters and change our state to be in a block.

If we end a block comment and we are in a block, then we will skip over the next two characters and change our state to be not in a block.

If we start a line comment and we aren't in a block, then we will ignore the rest of the line.

If we aren't in a block comment (and it wasn't the start of a comment), we will record the character we are at.

At the end of each line, if we aren't in a block, we will record the line.
'''
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        #my idea. find substring
        '''
        res = []
        blockCheckMark = False
        
        def blockCheck(lineIndx, source, line):
            pairRemain = line[:line.find('/*')]
            for i in range(lineIndx+1,len(source)):
                line = source[i]
                if line.find('*/') >= 0:
                    return (pairRemain+line[line.find('*/')+2:], i)
    
        
        lineIndx = 0
        line = source[lineIndx]
        while lineIndx < len(source):
            #checkBlock
            if not blockCheckMark:
                line = source[lineIndx]
            
            #case // /* */ or // first
            double = line.find('//')
            one = line.find('/*')
            if (double >=0 and one >= 0 and double < one) or (double >= 0 and one < 0):
                line = line[:double]
            
            #case /* // */
            l = [i for i in range(len(line)) if line.startswith('*/', i)]
            double = line.find('//')
            while l:
                if (double >= 0 and l[0] >= 0 and double > l[0]) or (double < 0 and l[0] >= 0):
                    r = [i for i in range(len(line)) if line.startswith('*/', i)]
                    for r_ind in range(len(r)):
                        if r[r_ind]-l[0] != 1:
                            line = line[:l[0]]+line[r[r_ind]+2:]
                            break
            
            #case // last
            ind = line.find('//')
            if ind >= 0:
                line = line[:ind]
            
            #case three /* block */
            l = line.find('/*')
            r = line.find('*/')
            if (l >= 0 and r < 0) or ( l >= 0 and r >= 0 and r - l == 1):
                line, lineIndx = blockCheck(lineIndx, source, line)
                blockCheckMark = True
                if line:
                    continue
            
            if line:
                res.append(line)
                
            blockCheckMark = False    
            lineIndx += 1
                
        return res
        '''
        #character
        res = []
        blockCheck = False
        
        for line in source:
            i = 0
            if not blockCheck:
                newLine = []
            
            while i < len(line):
                
                if line[i:i+2] == '/*' and not blockCheck:
                    blockCheck = True
                    i += 1
                elif line[i:i+2] == '*/' and blockCheck:
                    blockCheck = False
                    i += 1
                elif not blockCheck and line[i:i+2] == '//':
                    break
                elif not blockCheck:
                    newLine.append(line[i])
                i += 1
            if newLine and not blockCheck:
                res.append(''.join(newLine))
                
        return res
