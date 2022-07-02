class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary = set()
        self.abbreviation_res = defaultdict(list)
        self.create_dict(dictionary)
        self.abbreviation()

    def isUnique(self, word: str) -> bool:
        abbre_res = self.set_abbreviation(word)
        if abbre_res not in self.abbreviation_res or (len(self.abbreviation_res[abbre_res]) == 1 and word in self.dictionary):
            return True
        return False
    def abbreviation(self):
        for word in self.dictionary:
            self.abbreviation_res[self.set_abbreviation(word)].append(word)
    def set_abbreviation(self, word):
        prefix = word[0]
        suffix = ''
        middle = ''
        if len(word) > 2:
            prefix, suffix = word[0], word[-1]
            middle = str(len(word[1:-1]))
        elif len(word) == 2:
            suffix = word[-1]
        return prefix+middle+suffix
    def create_dict(self, dictionary):
        for word in dictionary:
            self.dictionary.add(word)
        
            


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)