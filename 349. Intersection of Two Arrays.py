class Solution(object):
    def intersection(self, nums1, nums2):
        k=[]
        for i in nums1:
            for j in nums2:
                if(i==j and i not in k):
                    k.append(i)
        return k
