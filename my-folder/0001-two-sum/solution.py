class Solution:
    def twoSum(self, nums, target):
        a = ()
        b = ()

        for i in range(len(nums)):
            for j in range(len(nums)):
                a = nums[i]
                b = nums[j]

                if a + b == target and i != j:
                    return [i, j]

