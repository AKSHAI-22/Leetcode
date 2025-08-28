class Solution(object):
    def findErrorNums(self, nums):
        dup=sum(nums)-sum(set(nums))
        miss=sum(range(1,len(nums)+1))-sum(set(nums))
        return [dup,miss]
