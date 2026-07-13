class Solution:
    def is_palindrome(self, s):
        n = len(s)
        left = 0
        right = n-1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def dfs(s):
            if not s:
                ans.append(path.copy())
                return
            
            n = len(s)
            for i in range(n):
                # try to add s[:i+1] if it's a palindrome
                if self.is_palindrome(s[:i+1]):
                    path.append(s[:i+1])
                    dfs(s[i+1:])
                    path.pop(-1)

        dfs(s)
        return ans