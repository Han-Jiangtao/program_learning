class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_num = nums[0]
        min_num = nums[0]
        max_diff = -1
        for num in nums:
            if num > max_num:
                max_diff = num - min_num if max_diff < num - min_num else max_diff
                max_num = num
            if num < min_num:
                max_num = num
                min_num = num
        return max_diff

