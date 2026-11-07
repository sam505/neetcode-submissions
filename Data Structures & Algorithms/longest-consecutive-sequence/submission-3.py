class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        len_1 = len_2 = 0
        numbers = sorted(set(nums))
        for i in range(len(numbers) - 1):
            if (numbers[i+1] - numbers[i]) == 1:
                len_1 += 1
            else:
                len_2 = max(len_2, len_1)
                len_1 = 0

        return max(len_1, len_2) + 1
        