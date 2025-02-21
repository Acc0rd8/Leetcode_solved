class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        stages = []
        
        while x >= 1 and y >= 4:
            stages.append(75 * x + y * 10)
            x -= 1
            y -= 4
        else:
            if len(stages) % 2 == 0:
                return 'Bob'
            return 'Alice'
    
print(Solution().winningPlayer(4, 11))