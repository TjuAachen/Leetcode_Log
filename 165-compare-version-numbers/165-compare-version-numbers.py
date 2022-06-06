class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        #split the version string by .
        split_v1 = version1.split('.')
        split_v2 = version2.split('.')
        
        #fill 0 to the shorted
        len_v1, len_v2 = len(split_v1), len(split_v2)
        if len_v1 < len_v2:
            split_v1.extend(['0']*(len_v2 - len_v1))
        else:
            split_v2.extend(['0']*(len_v1 - len_v2))
        
        
        #convert a str into a num
        def str2num(string):
            ans = 0
            for char in string:
                ans = ans*10 + int(char)
            return ans
        
        #convert version to an integer
        def version2num(version):
            ans = 0
            for char in version:
                number = str2num(char)
                ans = ans * 10 + number
            return ans
        num_v1, num_v2 = version2num(split_v1), version2num(split_v2)
        if num_v1 == num_v2:
            return 0
        if num_v1 < num_v2:
            return -1
        return 1
                
        