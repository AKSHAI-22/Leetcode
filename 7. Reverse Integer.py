class Solution(object):
    def reverse(self, x):
        n=abs(x)
        res=0
        while n!=0:
            l=n%10
            res=res*10+l
            n//=10
        if res < -2**31 or res > 2**31 - 1:
            return 0
        elif x<0:
            return -1*res
        else:
            return res
