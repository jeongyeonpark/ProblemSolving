class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        if n%2 != 0:
            bits += 1
            n -= 1

        n1 = int(n**(1/10))
        n2 = math.ceil(math.ceil(n/(10**n1))/2)
        q = (n1*3) + n2 

        if 2**q < n:
            q+=1
            
        while n > 0:
            if 2**q == n:
                bits += 10**q
                n = 0
            elif 2**q > n and 2**(q-1) <= n:
                bits += 10**(q-1)
                n -= 2**(q-1)
                q-=1
            else:
                q-=1
                """if 2**(int(q/2)) < n:
                    q = int(q/2)
                else:
                    q-=1"""


        print(bits)
        return str(bits).count('1')
        