class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums = sorted(nums)
        for i, num1 in enumerate(nums):
            if i > 0 and num1 == nums[i - 1]:
                continue
            total = None
            j = i + 1
            k = len(nums) - 1
            twosum = num1 * -1
            while  j < k:
                total = nums[j] + nums[k]
                if  total > twosum:
                    k -= 1
                elif total < twosum:
                    j += 1
                else:
                    solution.append([num1, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return solution