class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        non_set = set(['2','3','4','5','7'])
        map_num = dict()
        map_num['6'] = '9'
        map_num['9'] = '6'
        map_num['8'] = '8'
        map_num['0'] = '0'
        map_num['1'] = '1'
        reverse = num[::-1]
        for ind, char in enumerate(list(num)):
            if char in non_set:
                return False
            if map_num[char] != reverse[ind]:
                return False
        return True
            
            
        