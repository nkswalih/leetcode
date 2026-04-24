class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        return abs(moves.count('L') - moves.count('R')) + moves.count('_')