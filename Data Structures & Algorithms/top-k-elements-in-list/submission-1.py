class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqs = {}
        # for n in nums:
        #     freqs[n] = freqs.get(n, 0) + 1
        # most_to_least = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        # return [x[0] for x in most_to_least][:k]


        number_to_freq = {}  # {3:3,2:2,1:1}
        for n in nums:
            number_to_freq[n] = number_to_freq.get(n, 0) + 1
        freq_to_number = {}  # {3:[3],2:[2],1:[1]}
        for num, freq in number_to_freq.items():
            if freq not in freq_to_number:
                freq_to_number[freq] = []
            freq_to_number[freq].append(num)
        
        print(f"freq_to_number: {freq_to_number}")

        res = []
        for count in range(len(nums), 0, -1):  # 654321
            if count in freq_to_number:
                print(f"count {count}, adding {freq_to_number[count]} to res")
                res += freq_to_number[count]
                print(f"len(res) is now {len(res)}")
            if len(res) == k:
                return res
        
        


        
