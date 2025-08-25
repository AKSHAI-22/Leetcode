class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n   # base cases: 1 → 1 way, 2 → 2 ways
        
        a, b = 1, 2  # ways(1), ways(2)
        for i in range(3, n+1):
            a, b = b, a + b   # shift like Fibonacci
        return b
