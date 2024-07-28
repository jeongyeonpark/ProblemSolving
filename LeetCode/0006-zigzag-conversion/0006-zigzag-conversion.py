class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_array = [[] for _ in range(numRows)]
        if numRows == 1:
            return s
        elif numRows == 2:
            for _ in range(len(s)):
                if _%2 == 0:
                    s_array[0].append(s[_])
                else:
                    s_array[1].append(s[_])
        else:
            max_n = numRows
            s = s[::-1]
            while s:
                if max_n != numRows:
                    for num in range(numRows):
                        if max_n-1 == num:
                            s_array[num].append(s[-1])
                        else:
                            s_array[num].append('')
                    s = s[:-1]
                    if max_n <= 2:
                        max_n = numRows
                    else:
                        max_n-=1
                else:
                    s_ = s[-max_n:][::-1]
                    s = s[:-max_n]
                    for num in range(len(s_)):
                        s_array[num].append(s_[num])
                    max_n -=1

        output = ''
        for row in s_array:
            output+=''.join(row)
        return output