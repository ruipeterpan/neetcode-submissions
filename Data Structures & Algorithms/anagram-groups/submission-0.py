class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert each str into a freq dict. O(N) time, O(N) space
        
        # for each string, if we have seen its freq dict, add it to the list. 
        # If not, create a new list and add to that. 
        # Question: how do we maintain a dict -> list correspondence

        tuple_to_list = {}

        for s in strs:
            t = self.str_to_freq_tuple(s)
            if t in tuple_to_list.keys():
                tuple_to_list[t].append(s)
            else:
                tuple_to_list[t] = [s]
        return [x for x in tuple_to_list.values()]
    
    def str_to_freq_tuple(self, s):  # O(100) time, O(1) space
        freq = [0] * 26

        for c in s:
            idx = ord(c) - ord("a")
            freq[idx] += 1
        return tuple(freq)