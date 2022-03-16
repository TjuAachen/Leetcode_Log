class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        init = []
        index = 0
        while(index < len(pushed)):
            push_ele = pushed[index]
            if push_ele == popped[0]:
                popped.pop(0)
                pushed.pop(index)
                if index > 0:
                    index = index - 1
                else:
                    index = 0
            elif index < len(pushed) - 1:
                index = index + 1
            elif pushed:
                return False
        return True
            
            