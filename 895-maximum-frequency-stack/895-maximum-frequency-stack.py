class FreqStack:

    def __init__(self):
        self.stack = []
        self.valToFreq = {}
        self.valToPos = {}
        self.freqToVal = {}
        self.maxFreq = 0
        self.index = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.valToPos:
            self.valToPos[val].append(self.index)
        else:
            self.valToPos[val] = [self.index]
        self.index += 1
        if val in self.valToFreq:
            prev_freq = self.valToFreq[val]
            if prev_freq+1 in self.freqToVal:
                self.freqToVal[prev_freq+1].append(val)
            else:
                self.freqToVal[prev_freq+1] = [val]
            self.valToFreq[val] += 1
            self.maxFreq = max(prev_freq+1, self.maxFreq)
            
            
        else:
            self.valToFreq[val] = 1
            if 1 in self.freqToVal:
                self.freqToVal[1].append(val)
            else:
                self.freqToVal[1] = [val]
            self.maxFreq = max(self.maxFreq,1)
    def pop(self) -> int:
        cur_val = self.freqToVal[self.maxFreq][-1]
        position = self.valToPos[cur_val][-1]
        end = self.index
        cur_freq = self.valToFreq[cur_val]
        self.stack = self.stack[:position]+self.stack[position+1:]
        self.index = self.index - 1
        if self.valToFreq[cur_val] == 1:
            del self.valToFreq[cur_val]
        else:
            self.valToFreq[cur_val] = self.valToFreq[cur_val] - 1
        if len(self.valToPos[cur_val]) == 1:
            del self.valToPos[cur_val]
        else:
            self.valToPos[cur_val].pop()
        if len(self.freqToVal[cur_freq]) == 1:
            del self.freqToVal[cur_freq]
        else:
            self.freqToVal[cur_freq].pop()
        if self.maxFreq not in self.freqToVal:
            self.maxFreq = self.maxFreq - 1
        return cur_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()