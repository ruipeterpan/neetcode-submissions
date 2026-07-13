class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # construct a prefix array and a suffix array
        # prefix[i]: product of everything up until (excluding) i

        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = nums[i - 1] * prefix_product[i-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = nums[i + 1] * suffix_product[i+1]
        print(f"prefix_product: {prefix_product}")
        print(f"suffix_product: {suffix_product}")

        res = []
        for i in range(len(nums)):
            res.append(prefix_product[i] * suffix_product[i])
        return res