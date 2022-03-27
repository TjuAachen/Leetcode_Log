class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num = []
        res = []
        record = dict()
        for row in mat:
            mid = sum(row)
            num.append(mid)
            if mid in record:
                record[mid].append(len(num)-1)
            else:
                record[mid] = [len(num) - 1]
        num_sort = sorted(num)
        for index, elem in enumerate(num_sort):
            if index < k:
                result=record[num_sort[index]].pop(0)
                res.append(result)
        return res
            
        