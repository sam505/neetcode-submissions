class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_items = set(nums)

        if len(unique_items) != len(nums):
            return True
        else:
            return False
        