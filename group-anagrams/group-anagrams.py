class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        output = []
        for i in range(len(strs)):
            if tuple(sorted(strs[i])) not in result:
                result[tuple(sorted(strs[i]))] = [strs[i]]
            else:
                result[tuple(sorted(strs[i]))].append(strs[i])
        return result.values()