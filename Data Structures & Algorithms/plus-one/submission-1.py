class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number = int(''.join([str(d) for d in digits]))
        number += 1
        return [int(c) for c in str(number)]

        # digits.reverse()
        # n = len(digits)

        # for i in range()