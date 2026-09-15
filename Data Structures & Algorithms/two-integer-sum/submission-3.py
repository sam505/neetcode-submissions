class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        i != j and nums[i] + nums[j] = target
        """
        # length = len(nums)
        # for i in range(length):
        #     for j in range(length):
        #         if i == j:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        prevHash = {} # value: idx
        for i, n in enumerate(nums):
            

            diff = target - n
            if diff in prevHash:
                return [prevHash[diff], i]
            
            prevHash[n] = i
