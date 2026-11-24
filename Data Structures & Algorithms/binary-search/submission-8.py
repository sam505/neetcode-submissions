class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Sorted and distinct integers, looking for target
        option1: loop through the array checking for target O(n)
        option2: split array into half, check if the last first on left is greater than target
        """

        s = 0
        e = len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if target == nums[m]:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        return -1

