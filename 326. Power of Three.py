class Solution(object):
    def isPowerOfThree(self, n):
        i=0
        s=0
        while s<n:
            s=3**i
            if(s==n):
                return True
            i+=1
        return False
