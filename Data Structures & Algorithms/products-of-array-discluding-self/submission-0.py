class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for num in nums:
            product *= num

        if product == 0:
            product = 1
            idx = nums.index(0)
            nums.pop(idx)
            for num in nums:
                product *= num
            output = [0] * (len(nums) + 1)
            output[idx] = product
        else:
            output = [int(product/num) for num in nums]
        return output
            