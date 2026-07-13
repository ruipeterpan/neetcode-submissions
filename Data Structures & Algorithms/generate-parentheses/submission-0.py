class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = ""

        def dfs(left_brackets, right_brackets):
            nonlocal path
            if left_brackets == n and right_brackets == n:
                ans.append(path)
                return
            
            # case 1: can we add a (
            if left_brackets < n:
                path += "("
                dfs(left_brackets+1, right_brackets)
                path = path[:-1]

            # case 2: can we add a )
            if right_brackets < n and left_brackets > right_brackets: 
                path += ")"
                dfs(left_brackets, right_brackets+1)
                path = path[:-1]
        
        dfs(0, 0)
        return ans