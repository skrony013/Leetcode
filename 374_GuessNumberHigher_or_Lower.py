class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1, n
        while l<=r:
            m = (l+r)//2
            g = guess(m)
            if g == 0:
                return m
            elif g ==1:
                l = m+1
            else:
                r = m-1
        return -1

