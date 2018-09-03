#843 Guess the word
# idea comes form https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        '''
        #randomly guess
        #choose one of word, get n
        #update wordlist that in this wordlist, all word satisfied master.guess(guess) == n
        n = 0
        while n < 6:
            guess = random.choice(wordlist)
            n = master.guess(guess)
            wordlist = [word for word in wordlist if sum(i == j for i, j in zip(guess, word)) == n]
        '''
        #minimize the maximum possible size of the resulting wordlist
        #a better guess
        
        def match(w1, w2):
            return sum(i == j for i, j in zip(w1,w2))
        
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if match(w1, w2) == 0)
            #print count
            guess = min(wordlist, key=lambda w: count[w])
            #print guess
            n = master.guess(guess)
            wordlist = [w for w in wordlist if match(w, guess) == n]

