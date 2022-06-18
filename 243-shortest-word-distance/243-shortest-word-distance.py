class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_collection, word2_collection = [], []
        shortest_distance = float('inf')
        for ind, word in enumerate(wordsDict):
            if word == word1:
                word1_collection.append(ind)
                if word2_collection:
                    shortest_distance = min(shortest_distance, abs(word2_collection[-1] - ind) )
            if word == word2:
                word2_collection.append(ind)
                if word1_collection:
                    shortest_distance = min(shortest_distance, abs(word1_collection[-1] - ind) )                
        
        return shortest_distance 
        