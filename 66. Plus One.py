class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Traverse from the last digit
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0   # if digit is 9, make it 0 and carry over
        
        # If all digits were 9, we need an extra 1 at the beginning
        return [1] + digits
