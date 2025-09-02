class Solution(object):
    def sumOfUnique(self, nums):
        res = 0
        for n in nums:
            if nums.count(n) == 1:   # check if appears exactly once
                res += n
        return res
