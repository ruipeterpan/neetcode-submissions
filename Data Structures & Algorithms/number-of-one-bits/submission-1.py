class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        for _ in range(32):
            count += n & 1
            n = n >> 1
        
        return count

        """
        bin_str = bin(n)
        bin_str = bin_str[2:]

        return sum([1 for c in bin_str if c == "1"])
        """