class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        print(len(pattern), len(s.split()))
        if len(pattern) != len(s.split()):
            return False
        if (len(set(pattern)) == 1) and (len(set(s.split())) == 1):
            return True
        

        uniq_p = set(list(pattern))
        pat_list = {}
        for p in uniq_p:
            w_list = []
            for i in range(len(pattern)):
                if pattern[i] == p:
                    word = s.split()[i]
                    w_list.append(word)
            if len(set(w_list)) != 1:
                print('over uniq_p list len 1')
                return False
            elif not w_list[0] in pat_list:
                pat_list[w_list[0]] = p
            else:
                if pat_list[w_list[0]] != p:
                    print('not  match pattern')
                    return False
        return True

        
