class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_helper(i, j, target):
            # search within a sublist, where nums[i] is the leftmost
            # element, and nums[j] is the rightmost element.
            if i == j:
                if nums[i] == target:
                    return i
                else:
                    return -1
             
            if i > j:
                return -1
            
            middle_point = (i + j) // 2
            # print(f"i {i}, j {j}, middle_point {middle_point}")

            if nums[middle_point] == target:
                return middle_point
            elif nums[middle_point] < target:
                return search_helper(middle_point + 1, j, target)
            elif nums[middle_point] > target:
                return search_helper(i, middle_point - 1, target)
        
        return search_helper(0, len(nums) - 1, target)

