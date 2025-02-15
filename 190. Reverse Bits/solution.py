class Solution:
    def reverseBits(self, n: int) -> int:
        numbers_bits = str(bin(n))[2:]
        reversed_bits = numbers_bits[::-1]
        
        if len(reversed_bits) != 32:
            reversed_bits += '0' * (32 - len(reversed_bits))
        
        return int(reversed_bits, 2)