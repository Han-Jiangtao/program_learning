class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        now = 0
        min_len = len(nums) + 1
        for _idx, _item in enumerate(nums):
            now += _item
            end = _idx

