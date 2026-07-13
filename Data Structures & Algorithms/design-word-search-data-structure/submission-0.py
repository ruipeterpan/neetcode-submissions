class TrieNode:
    def __init__(self):
        # self.val = val
        self.map = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i, ch in enumerate(word):
            if ch not in curr.map:
                curr.map[ch] = TrieNode()
            curr = curr.map[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:

        def search_helper(node, word):
            if len(word) == 0:
                return node.is_word
            ch = word[0]
            if ch == ".":
                return any(
                    [search_helper(n, word[1:]) 
                    for ch, n in node.map.items()])
            else:
                if ch not in node.map:
                    return False
                return search_helper(node.map[ch], word[1:])
        
        return search_helper(self.root, word)

