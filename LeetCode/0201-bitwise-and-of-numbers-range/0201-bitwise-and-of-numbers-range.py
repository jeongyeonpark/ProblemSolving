class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 and right == 1:
            return 0
            
        def return_bitwise(num):
            if num == 0:
                return ""
            n = 0
            num_ = num
            while num_ >= 2:
                num_ = num_/2
                n+=1

            bitwise = [0]*(n+1)
            while n>=0:
                if num >= 2**n and num < (2**(n+1)):
                    bitwise[-n-1] = 1
                    num-=2**n
                n-=1
            return bitwise

        res  = [0]*(len(return_bitwise(left))+1)
        x = 0
        NUM = left if left!=0 else 1
        while NUM <= right:

            bitwise_ = return_bitwise(NUM)
            for i in range(1,min(len(bitwise_)+1,len(res)+1)):
                res[-i]+=bitwise_[-i]
            x+=1

            if NUM == right:
                break

            for i in range(len(bitwise_)-1, -1, -1):
                if 2**(i) <= right-NUM:
                    NUM += 2**(i)
                    for y in range(1,min(i+1, len(res)+1)):
                        res[-y] = 0
                    break

        result = 0
        for i in range(1,len(res)+1):
            if res[-i] == x and res[-i]!=0:
                result+=2**(i-1)
        return result