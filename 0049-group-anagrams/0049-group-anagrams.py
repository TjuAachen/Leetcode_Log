class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        
        for str in strs:
            key, val= ''.join(sorted(str)), str
            result[key].append(val)
        
        return list(result.values())
        