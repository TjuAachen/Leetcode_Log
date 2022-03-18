class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        record = dict()
        n = len(s)
        for index,char in enumerate(s):
            if char in record:
                record[char].append(index)
            else:
                record[char] = [index]
        visited = dict()
        track = []
        for i in range(n):
            cur = s[i]
            if cur not in track:
                while(track):
                    if cur < track[-1] :
                        if i < record[track[-1]][-1]:
                            track.pop()
                        else:
                            break
                    else:
                        break
                track.append(cur)
        return ''.join(track)
                        
                
        
                    
        
        