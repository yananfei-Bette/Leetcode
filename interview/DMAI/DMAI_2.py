
def solution(stroke_data, char_list, char_to_strokes):
    # Type your solution here
    # some ideas
    # first convert stroke data to string cadidates
    # my idea is, use backtrack to find all possible strings
    # but, in order to reduce some time complexity
    # i use 0 to split stroke data. convert into substroke list. 
    # each substroke represent one word
    # stroke_words = [[]]
    
    # seconde calculate log likelihood to find the best
    # res = ""
    # maxProb = float("inf")

    
    # split stroke data
    stroke_words = []
    word = []
    for i in range(len(stroke_data)):
        if stroke_data[i] != 0:
            word.append(stroke_data[i])
        else:
            stroke_words.append(word)
            word = []
    stroke_words.append(word)
    # print(stroke_words)
    '''
    [[3, 6, 2, 3, 1, 8, 2, 4, 5], 
    [8, 2, 5, 4], 
    [4, 2, 1], 
    [7, 4, 3, 2, 1, 4, 1, 6, 2, 4, 1, 3, 6], 
    [6, 3, 6, 4, 1, 5, 4, 3, 6], 
    [4, 2, 4, 1, 4, 5, 1, 6, 4, 8]]
    '''


    # convert char_to_strokes type, from list(strings) to set(sort_list)
    char_to_strokes_set = set()
    for s in char_to_strokes:
        s_set = tuple(sorted(s.split(" ")))
        char_to_strokes_set.add(s_set)
    # print(char_to_strokes_set)
    '''
    {('3', '5'), ('1', '2', '4'), ('1', '4', '6'), 
    ('1', '2'), ('1', '3', '6'), ('2', '8'), ('10', '9'), 
    ('10', '10', '9', '9'), ('3', '6'), ('1', '2', '2'), ('4',), 
    ('3',), ('10', '9', '9'), ('4', '5'), ('3', '4'), ('1', '2', '3'), 
    ('3', '7', '8'), ('6', '6', '9'), ('10', '3', '9'), ('0',), ('8',), 
    ('1', '1', '2', '2', '2'), ('2', '2', '7'), ('3', '4', '7')}
    '''
    
    # for each stroke word, use backtrack to find all candidate strings.
    # use dic to save(index of stroke_words, [candidate strings])
    ##################### backtrack #######################
    def backtrack(word, res, curr, ind, char_to_strokes_set, char_list):
        if ind == len(word):
            res.append(curr)
            return res
        if ind > len(word):
            return res

        # for i in range(ind, len(word)):
        for i in range(ind, len(word)):

            candidate = tuple(sorted([str(num) for num in word[ind: i + 1]]))

            if candidate in char_to_strokes_set:
                # find candidate
                for index, stroke in enumerate(char_to_strokes):
                    if candidate == tuple(sorted(stroke.split(" "))):
                        
                        candidate_char = char_list[index]

                        # call backtrack
                        res = backtrack(word, res, curr + candidate_char, i + 1, char_to_strokes_set, char_list)
        
        return res   
    #######################################################
    dic = {}
    for i, word in enumerate(stroke_words):
        candidate_strings = backtrack(word, [], "", 0, char_to_strokes_set, char_list)
        # print(word, candidate_strings)
        dic[i] = candidate_strings
        # break
    # print(dic)
    '''
    {0: ['thio', 'this'], 1: ['io', 'is'], 2: ['cr', 'a'], 
    3: ['great'], 4: ['teot', 'test'], 5: ['caoe.', 'case.']}
    '''

    #####################################################################################

    # convert char_list to char_list_dic
    char_list_dic = {}
    for i, val in enumerate(char_list):
        char_list_dic[val] = i
    # print(char_list_dic)
    '''
    {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 
    'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26, '.': 27}
    '''


    # we have words. Now what we need to do is combine those words to get strings
    # there is a trick, we can count words' n-gram likelihood first.
    # For exmaple 
    # in this case, we can count " this ", " is ", " a ", " great ", " test ", " case."
    # we only need to add some spaces in and count the word.
    dic_with_lprob = {}
    for key, words in dic.items():
        val = []
        for word in words:
            ngram_to_lprob_val = 0
            for i, char in enumerate(word):
                if i == 0:
                    indexSpace = char_list_dic[" "]
                    indexChar = char_list_dic[char]
                    # ngram_to_lprob_val += ngram_to_lprob[indexSpace][indexChar]
                else:
                    indexSpace = char_list_dic[word[i - 1]]
                    indexChar = char_list_dic[char]
                    # ngram_to_lprob_val += ngram_to_lprob[indexSpace][indexChar]
            if key != len(dic.items()) - 1:
                indexChar = char_list_dic[word[-1]]
                indexSpace = char_list_dic[" "]
                # ngram_to_lprob_val += ngram_to_lprob[indexChar][indexSpace]

            val.append([word, ngram_to_lprob_val])
        dic_with_lprob[key] = val



        
'''
stroke_data = [3,6,2,3,1,8,2,4,5,0,
                8,2,5,4,0,
                4,2,1,0,
                7,4,3,2,1,4,1,6,2,4,1,3,6,0,
                6,3,6,4,1,5,4,3,6,0,
                4,2,4,1,4,5,1,6,4,8]

char_list = ["a","b","c","d","e","f","g",
                "h","i","j","k","l","m","n",
                "o","p","q","r","s","t",
                "u","v","w","x","y","z",
                " ","."]

char_to_strokes = ["4 1 2","3 5","4","4 3","4 1 6","3 1 6","4 3 7",
                    "3 1 2","2 8","7 3 8","3 9 10","3","2 1 2 1 2","2 1 2",
                    "4 5","3 5","4 3","2 1","4 5","3 6",
                    "2 7 2","10 9","10 9 10 9","10 9","10 9 9","6 9 6",
                    "0","8"]
'''
stroke_data = [9,9,10,4,5,7,2,2,0,
                1,6,3,5,4,7,2,2,1,2,2,4,3,0,
                3,6,1,3,2,4,1,6,0,
                2,2,1,1,2,1,6,4,1,2,4,2,1,2,8,2,2,1,2,3,7,4,0,
                5,4,3,6,1,0,
                3,6,1,2,3,2,8,5,4,0,
                2,2,1,2,1,1,4,6,5,4,5,4,1,2,4,7,4,3,1,4,6,8]

char_list = ["a","b","c","d","e","f","g",
                "h","i","j","k","l","m","n",
                "o","p","q","r","s","t",
                "u","v","w","x","y","z",
                " ","."]

char_to_strokes = ["4 1 2","3 5","4","4 3","4 1 6","3 1 6","4 3 7",
                    "3 1 2","2 8","7 3 8","3 9 10","3","2 1 2 1 2","2 1 2",
                    "4 5","3 5","4 3","2 1","4 5","3 6",
                    "2 7 2","10 9","10 9 10 9","10 9","10 9 9","6 9 6",
                    "0","8"]  
   
print(solution(stroke_data, char_list, char_to_strokes))













