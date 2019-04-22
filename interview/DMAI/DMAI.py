
def solution(min_exercise_len, max_exercise_len, lesson_len):
    # Type your solution here 
    
    # it is a question which is similiar to coin chage
    # there are several ways to solve: like backtrack and DP
    
    # dp
    # find min_lessons
    '''
    dpMin = [float("inf")] * (lesson_len + 1)
    dpMin[0] = 0
    for i in range(1, lesson_len + 1):
        for j in range(min_exercise_len, max_exercise_len + 1):
            if j <= i:
                if i - j - 5 >= 0:
                    dpMin[i] = min(dpMin[i], dpMin[i - j - 5] + 1)
                else:
                    dpMin[i] = min(dpMin[i], 1)
    print(dpMin)
    
    min_exercise_len = dpMin[-1] if dpMin[-1] <= lesson_len else -1
    
    # find max_lessons
    dpMax = [float("-inf")] * (lesson_len + 1)
    dpMax[0] = 0
    for i in range(1, lesson_len + 1):
        for j in range(min_exercise_len, max_exercise_len + 1):
            if j <= i:
                if i - j - 5 >= 0:
                    dpMax[i] = max(dpMax[i], dpMax[i - j - 5] + 1)
                else:
                    dpMax[i] = max(dpMax[i], 1)
    
    max_exercise_len = dpMax[-1] if dpMax[-1] >= 0 else -1
    
    return [min_exercise_len, max_exercise_len]
    '''
    min_lesson = float("inf")
    max_lesson = float("-inf")
    
    def backtrack(lesson_len, l, max_exercise_len, curr_len, min_lesson, max_lesson):
        #print(lesson_len, l, max_exercise_len, curr_len, min_lesson, max_lesson)
        if lesson_len == 0:
            min_lesson = min(min_lesson, curr_len)
            max_lesson = max(max_lesson, curr_len)
            return [min_lesson, max_lesson]
        for i in range(l, max_exercise_len + 1):
            if lesson_len - i - 5 > 0:
                #print(">5")
                min_lesson, max_lesson = backtrack(lesson_len - i - 5, i, max_exercise_len, curr_len + 1, min_lesson, max_lesson)
            elif 0 <= lesson_len - i <= 5:
                #print("<5")
                min_lesson, max_lesson = backtrack(0, i, max_exercise_len, curr_len + 1, min_lesson, max_lesson)
            else:
                #print("<0")
                min_lesson, max_lesson = backtrack(0, i, max_exercise_len, curr_len, min_lesson, max_lesson)
        return [min_lesson, max_lesson]
        
    min_lesson, max_lesson = backtrack(lesson_len, min_exercise_len, max_exercise_len, 0, min_lesson, max_lesson)

    return [
        min_lesson if min_lesson != float("inf") else -1,
        max_lesson if max_lesson != float("-inf") else -1
    ]
    

print(solution(1, 3, 1000), [126, 167])












