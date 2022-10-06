class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        #find the maximum number no more than damage
        maxTarget = 0
        res = 0
        for curDamage in damage:
            if curDamage > maxTarget and curDamage <= armor:
                maxTarget = curDamage
            if curDamage > armor:
                maxTarget = armor
            res += curDamage
        return res + 1 - maxTarget