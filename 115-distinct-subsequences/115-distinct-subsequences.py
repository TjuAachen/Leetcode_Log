class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = dict()
        def num(res, target):
            if len(target) == 0:
                return 1
            if len(res) == 0:
                return 0
            if (res, target) in result:
                return result[(res, target)]
            if res[0] == target[0]:
                result[(res, target)] = num(res[1:], target[1:]) + num(res[1:], target)
                return result[(res, target)]
            result[(res, target)] = num(res[1:],target)
            return result[(res, target)]
        num(s, t)
        return result[(s,t)]
        
                        
            
        
        