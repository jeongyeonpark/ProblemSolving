class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        position = len(str(num))
        result = ''
        while position!=0:
            n = int(str(num)[len(str(num))-position])*(10**(position-1))
            if n != 0:
                if n in symbols:
                    result+=symbols[n]
                else:
                    x = str(n)[0]
                    y = symbols[n/int(x)]
                    if x in ['2','3']:
                        result+=y*int(x)
                    elif x in ['6','7','8']:
                        x1 = 5
                        x2 = int(x)-5
                        result+=symbols[x1*(10**(position-1))]
                        result+=x2*symbols[10**(position-1)]
            position-=1
        return result