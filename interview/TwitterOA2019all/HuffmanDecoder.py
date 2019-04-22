#HuffmanDecoder
def huffmanDecoder(codeMap, codeInput):
    if not codeInput:
        return ''

    dic = {}
    for i in range(len(codeMap)):
        value, key = codeMap[i].split('	')
        if value == 'newline':
            value = '\n'
        dic[key] = value
    
    resString = ''
    winStr, winEnd = 0, 1
    while winStr < len(codeInput) and winEnd <= len(codeInput):
        subInput = codeInput[winStr:winEnd]
        if subInput in dic.keys():
            resString += dic[subInput]
            winStr, winEnd = winEnd, winEnd+1
        else:
            winEnd += 1
    return resString

codeMap = ["a	100100", "b	100101", "c	110001", "d	100000", "newline	1111111", "p	111110", "q	000001"]
codeInput = "1111100000011001001111111100101110001111110"
print(huffmanDecoder(codeMap, codeInput))
