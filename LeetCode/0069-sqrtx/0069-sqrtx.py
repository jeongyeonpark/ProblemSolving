class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        n = int(x/2)
        while x:
            if n*n == x:
                return n
            elif n*n < x:
                if (n+1)*(n+1) > x:
                    return n
                else:
                    if (n*n - x) > x:
                        n = n*2
                    else:
                        n+=1
            elif n*n > x:
                if (n-1)*(n-1) < x:
                    return n-1
                else:
                    if (x - n*n) < x:
                        n = int(n/2)
                    else:
                        n-=1