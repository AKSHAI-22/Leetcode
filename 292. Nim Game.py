class Solution(object):
    def canWinNim(self, n):
        if(n<=3):
            return True
        else:
            if(n%4==0):
                return False
            else:
                return True

        
