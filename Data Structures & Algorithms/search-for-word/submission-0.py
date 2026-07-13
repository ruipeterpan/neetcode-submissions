class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        a = len(board)
        b = len(board[0])

        path = []

        def dfs(i, j, k):
            # returns True if we can get a match using a
            # path that starts at [i, j], and the remaining word is word[k:]
            if i < 0 or i >= a or j < 0 or j >= b:
                return False

            if board[i][j] != word[k]:
                return False
            
            if k == word_len - 1:
                return True

            path.append((i, j))
            # this immediate one is correct, but have remaining words to match
            next_steps = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for next_i, next_j in next_steps:
                if (next_i, next_j) not in path:
                    if dfs(next_i, next_j, k+1):
                        return True
            path.pop()
            return False
    
        for i in range(a):
            for j in range(b):
                if dfs(i, j, 0):
                    return True
        return False



