class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        allWinner = []
        lostOneMatch = []
        
        playerLoseTime = defaultdict(int)
        players = set()
        
        for winner, loser in matches:
            playerLoseTime[loser] += 1
            players.add(winner)
            players.add(loser)
        

        for loser, time in playerLoseTime.items():
            if time == 1:
                lostOneMatch.append(loser)
            players.remove(loser)
        
        res = []
        
        players = sorted(list(players))
        lostOneMatch.sort()
        
        res.append(players)
        res.append(lostOneMatch)
        
        return res
                
        