class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        b=0
        for i in a:
            if i - 1 not in a:
                z=i
                c=1
                while z + 1 in a:
                    z+=1
                    c+=1
                b=max(b, c)
        return b
        
