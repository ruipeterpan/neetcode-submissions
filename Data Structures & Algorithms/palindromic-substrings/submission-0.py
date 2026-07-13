class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointer solution
        n = len(s)

        num_total_palindromes = 0

        for i in range(n):
            # 2 cases for a palindrome: 
            # 1. if i is the middle, we expand two pointers to the left and right
            x, y = i, i
            while x >= 0 and y <= n-1 and s[x] == s[y]:
                num_total_palindromes += 1
                x -= 1
                y += 1
            
            # 2. if i is to the left of the true center of a even-length palindrome, 
            # two pointers are on i and i+1; continue to expand right
            x, y = i, i+1
            while x >= 0 and y <= n-1 and s[x] == s[y]:
                num_total_palindromes += 1
                x -= 1
                y += 1
        
        return num_total_palindromes
