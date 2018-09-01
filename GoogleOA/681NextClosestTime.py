# 681 Next Closet Time

#from datetime import *
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        '''
        #bf
        #O(1440)
        s = set(time)
        hour = int(time[0:2])
        minute = int(time[3:])
        while True:
            minute += 1
            if minute == 60:
                minute = 0
                hour = 0 if hour == 23 else hour+1
            
            time = "%02d:%02d" % (hour, minute)
            if set(time) <= s:
                return time
        return time
        '''
        '''
        # datetime        
        s = set(time)
        #print s
        while True:
            time = (datetime.strptime(time, '%H:%M')+
                    timedelta(minutes=1)).strftime('%H:%M')
            if set(time) <= s:
                return time
        return time
        '''
        #dfs
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
            #print h1, h2, m1, m2
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapsed = (cur - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed

        return "{:02d}:{:02d}".format(*divmod(ans, 60))
