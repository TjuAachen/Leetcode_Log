class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n_start, n_target = len(start), len(target)
        i, j = 0, 0
        while(i < n_start and j < n_target):
            while(i < n_start and start[i] == '_'):
                i = i + 1
            while(j < n_target and target[j] == '_'):
                j = j + 1
            start_str = None
            target_str = None
            if i < n_start:
                start_str = start[i]
            if j < n_target:
                target_str = target[j]
            if start_str == target_str == 'R':
                if i > j:
                    return False
            if start_str == target_str == 'L':
                if i < j:
                    return False
            if start_str != target_str:
                return False
            i = i + 1
            j += 1
        remaining_target, remaining_start = '',''
        if j < n_target:
            remaining_target = target[j:].strip('_')
        if i < n_start:
            remaining_start = start[i:].strip('_')
        if remaining_target == remaining_start:
            return True
        return False
                
        
        
        
        
    
            
        