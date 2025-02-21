class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start_position = [0, 0]
        position = [0, 0]
        
        for move in moves:
            if move == 'L':
                position[0] -= 1
            elif move == 'R':
                position[0] += 1
            elif move == 'U':
                position[1] += 1
            elif move == 'D':
                position[1] -= 1
            else:
                return False
        
        return True if position == start_position else False