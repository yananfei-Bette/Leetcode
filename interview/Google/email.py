#email

def numSameEmailAddress(s):
    dic = {}
    for email in s:
        local, domain = email.split('@')
        local = ''.join(email.split('.'))
        while local.find('+') >= 0:
            local = local[:local.find('+')]
        email = local+'@'+domain
        if email not in dic:
            dic[email] = 1
        else:
            dic[email] += 1
    res = 0
    for k in dic.keys():
        if dic[k] > 1:
            res += 1
    return res
    #sorted(mydict.items(), key=lambda item: (item[1], item[0]))
    #sorted_d = sorted((value, key) for (key,value) in d.items())
    #print(sorted(dic.items(), key = lambda x : (x[1], x[0])))
    #return sorted(dic.items(), key = lambda x : (x[1], x[0]))[-1][1]

if __name__ == "__main__":
    s = ['yananfei@usc.edu', 'yananfei+abc@usc.edu', 'yanantry...2dfs@usc', 'yanan.fei@usc.edu']
    print('********result********')
    print(numSameEmailAddress(s))
