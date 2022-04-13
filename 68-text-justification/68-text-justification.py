class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        count = 0
        final = []
        def combine(line,count):
            if len(line) < 2:
                extra, add= -1, maxWidth -count               
            else:
                extra = (maxWidth-count)//(len(line)-1)
                add = (maxWidth-count) %(len(line)-1)
            if extra == -1:
                if line:
                    line[0] = line[0] + ' '*add
                else:
                    line = ' '*add
            else:
                for j in range(len(line)-1):
                    if add > 0:
                        num_space = ' '*(extra+1+1)
                        add = add - 1
                    else:
                        num_space = ' '*(extra+1)
                    line[j+1] = num_space +line[j+1]                 
            return line
        for word in words:
            if not line:
                line.append(word)
                count = len(word)
            elif count + len(word) + 1<= maxWidth:
                line.append(word)
                count += len(word) + 1
            else:
                line = combine(line[:], count)
                line = ''.join(line)                
                final.append(line)
                line = [word]
                count = len(word)
        if line:
            line = ' '.join(line) + (maxWidth-count)*' '
            final.append(line)
        return final
                
                
                
            
            
        