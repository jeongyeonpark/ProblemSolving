class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        head_index = 0
        long_pal_string = ''

        while head_index<len(s)-len(long_pal_string):
            for tail_index in range(len(s)-1, head_index-1, -1):
                if len(long_pal_string)>(tail_index-head_index+1):
                    break
                h_idx = head_index
                t_idx = tail_index
                head_string = ''
                tail_string = ''
                while h_idx<=t_idx:
                    if s[h_idx] != s[t_idx]:
                        break
                    if h_idx==t_idx:
                        head_string+=s[h_idx]
                    elif s[h_idx] == s[t_idx]:
                        head_string+=s[h_idx]
                        tail_string = s[t_idx]+tail_string
                    h_idx+=1
                    t_idx-=1
                if len(head_string+tail_string) == (tail_index-head_index+1):
                    if len(head_string+tail_string) > len(long_pal_string):
                        long_pal_string = head_string+tail_string
            head_index+=1
        return long_pal_string if long_pal_string else s[0]