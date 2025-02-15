class Solution:
    def hammingWeight(self, n: int) -> int:
        mock_binary = str(bin(n))
        return mock_binary.count(1)