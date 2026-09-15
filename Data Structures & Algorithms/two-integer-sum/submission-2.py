class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        i != j and nums[i] + nums[j] = target
        """
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]


        for i in range(len(nums)):
            num_j = target - nums[i]
            if num_j in nums:
                j = nums.index(num_j)
                if i == j:
                    continue
                return [i, j]
                