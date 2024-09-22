def solution(friends, gifts):
    gift_n = {}
    for f in friends:
        gift_n[f] = {'total':0}
        for y in friends:
            if f!= y:
                gift_n[f][y] = 0

    for gift in gifts:
        x,y = gift.split()[0],  gift.split()[1]
        gift_n[x][y] +=1
        gift_n[x]['total'] +=1
        gift_n[y]['total'] -=1

    result = {f:0 for f in friends}
    done_list = set()
    for freind in gift_n:
        freinds_list = [x for x in gift_n[freind] if not x == 'total']
        for f in freinds_list:
            if not '_'.join(sorted([freind, f])) in done_list:
                n1 =  gift_n[freind][f]
                n2 = gift_n[f][freind]
                if n1>n2:
                    result[freind]+=1
                elif n1<n2:
                    result[f]+=1
                else:
                    if gift_n[freind]['total'] > gift_n[f]['total']:
                        result[freind]+=1
                    elif gift_n[f]['total'] > gift_n[freind]['total']:
                        result[f]+=1
                done_list.add('_'.join(sorted([freind, f])))
                
    return max(result.values())