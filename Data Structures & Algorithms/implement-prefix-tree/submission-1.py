class TrieNode:
    def __init__(self):
        # self.val = val
        self.map = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, ch in enumerate(word):
            if ch not in curr.map:
                curr.map[ch] = TrieNode()
            curr = curr.map[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, ch in enumerate(word):
            if ch not in curr.map:
                return False
            curr = curr.map[ch]
        return curr.is_word
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, ch in enumerate(prefix):
            if ch not in curr.map:
                return False
            curr = curr.map[ch]
        return True
        
        