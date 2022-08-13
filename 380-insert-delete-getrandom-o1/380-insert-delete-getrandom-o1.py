import random
class RandomizedSet:

    def __init__(self):
        self.val_to_index = dict()
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        new_index = len(self.array)
        self.val_to_index[val] = new_index
        self.array.append(val)
        return True
    

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        del self.val_to_index[val]
        if index != len(self.array) - 1:
            self.array[index], self.array[-1] = self.array[-1], self.array[index]
            self.val_to_index[self.array[index]] = index
        self.array.pop()
        return True
    def getRandom(self) -> int:
        selected_index = random.randint(0, len(self.array) - 1)
      #  print(self.array)
        return self.array[selected_index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()