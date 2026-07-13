class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        ans = []
        path = ""
        n = len(digits)

        def dfs(i):
            nonlocal path 
            if i == n:
                ans.append(path)
                return
            
            for c in mapping[digits[i]]:
                path += c
                dfs(i+1)
                path = path[:-1]

        dfs(0)
        return ans
