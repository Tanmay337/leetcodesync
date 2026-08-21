import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1 = []

        if nums.count(0) > 1:
            return [0] * len(nums)

        if nums.count(0) == 1:
            zero_index = nums.index(0)

            nums_without_zero = nums.copy()
            nums_without_zero.remove(0)

            product = math.prod(nums_without_zero)

            l1 = [0] * len(nums)
            l1[zero_index] = product

            return l1

        product = math.prod(nums)

        for num in nums:
            l1.append(product // num)

        return l1
