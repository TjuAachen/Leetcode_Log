import random
class RandomizedCollection(object):

    def __init__(self):
        self.val_to_num = defaultdict(deque)
        self.array = []
        self.pair_to_index = defaultdict(list)
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        is_present = True
        if val in self.val_to_num:
            is_present = False
        index = len(self.array)
        nxt_num = 0
        if not is_present:
            nxt_num = self.val_to_num[val][-1] + 1
        self.array.append((val, nxt_num))
        self.pair_to_index[(val, nxt_num)] = index
        self.val_to_num[val].append(nxt_num)
        
        return is_present

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_num:
            return False
        
        num = self.val_to_num[val].popleft()
        selected_index = self.pair_to_index[(val, num)]
        del self.pair_to_index[(val, num)]
        
        if not self.val_to_num[val]:
            del self.val_to_num[val]
      #  selected_index = index.pop()
      #  print(self.array)
        if selected_index == len(self.array) - 1:
            self.array.pop()
        
        else:
           # print(selected_index, self.array, val, num)
            self.array[-1], self.array[selected_index] = self.array[selected_index], self.array[-1]
            self.array.pop()
            cur_num = self.array[selected_index][-1]
            self.pair_to_index[(self.array[selected_index][0], cur_num)] = selected_index
           # print(self.array[selected_index], cur_num, selected_index)
            
        return True 

        
    def getRandom(self):
        """
        :rtype: int
        """
        choice = random.randint(0, len(self.array) - 1)
        return self.array[choice][0]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()