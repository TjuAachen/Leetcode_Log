class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        global final
        final = 10**10
        record = dict()
        if word2 == '':
            return len(word1)
        if word1 == '':
            return len(word2)
        def find(word_1, word_2):
            if (word_1, word_2) in record:
                return record[(word_1,word_2)]
            if word_1 == word_2:
                record[(word_1,word_2)] = 0
                return 0
            if not word_2:
                record[(word_1,word_2)] = len(word_1)
                return len(word_1)
            if not word_1:
                record[(word_1,word_2)] = len(word_2)
                return len(word_2)
            if word_1[0] == word_2[0]:
                ans = find(word_1[1:],word_2[1:])
            else:
                #insert
                a = find(word_2[0]+word_1,word_2) + 1
                #delete
                b = find(word_1[1:],word_2) + 1
                #replace
                c = find(word_2[0]+word_1[1:],word_2)+1
                ans = min([a,b,c])
            record[(word_1,word_2)] = ans
            return ans
        return find(word1,word2)
                
                
            
        
                
            