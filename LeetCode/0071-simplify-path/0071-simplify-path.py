class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == '/../' or path == '/..' or path == '/' or path == '/.' or path == '/./':
            return '/'

        n=1
        w = 0
        d = 0
        new_path = '/'
        for i in range(1,len(path)):
            if path[i] == '/' or i == len(path)-1:
                if path[i] != '/':
                    if n == 0:#
                        new_path+='/'#
                    new_path += path[i]
                    
                    if path[i] == '.':
                        d+=1
                    else:
                        w +=1

                if w == 0 and d == 0:
                    pass
                elif d == 0:
                    w = 0
                    n = 0
                elif w == 0:
                    if d == 1:
                        new_path = new_path[:-2]
                        n=0
                    elif d == 2:
                        if len(new_path.split('/')) < 4:
                            new_path = '/'
                            n = 1
                        else:
                            new_path = '/'.join(new_path.split('/')[:-2])
                            n=0
                    else:
                        n = 0
                    d = 0
                else:
                    w, d, n = 0, 0, 0

            else:
                if n==0:
                    new_path+='/'
                    n=1
                 
                if path[i] == '.':
                    d +=1
                    new_path+='.'
                else:
                    w +=1
                    new_path+=path[i]

        if len(new_path)==0:
            return '/'
        elif len(new_path) != 1 and new_path[-1] == '/':
             return new_path[:-1]
        else:
            return new_path