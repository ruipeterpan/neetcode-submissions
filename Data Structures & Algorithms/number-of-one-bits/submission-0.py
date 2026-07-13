class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = bin(n)
        bin_str = bin_str[2:]

        return sum([1 for c in bin_str if c == "1"])