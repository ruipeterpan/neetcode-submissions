class Solution:

    def encode(self, strs: List[str]) -> str:
        # "Hello" -> "5#Hello"
        result = ""
        for s in strs:
            num_chars = len(s)
            result += f"{num_chars}#{s}"
        print(f"Encoded str {result}")
        return result


    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            j = i
            len_str = ""
            while s[j] != "#":
                len_str += s[j]
                j += 1
            length = int(len_str)
            word = s[j + 1:j + 1 + length]
            result.append(word)
            i = j + 1 + length
        
        return result
            
