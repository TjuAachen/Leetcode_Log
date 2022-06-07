class TwoSum:

    def __init__(self):
        self.hash = dict()

    def add(self, number: int) -> None:
        if number not in self.hash:
            self.hash[number] = 1
        else:
            self.hash[number] += 1

    def find(self, value: int) -> bool:
        for key in self.hash.keys():
            if value - key == key and self.hash[key] > 1:
                return True
            if value - key != key and value - key in self.hash:
                return True   
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)