from collections import defaultdict
def solution(points, routes):
    answer = 0
    robots = len(routes)
    curr_positions = {}
    destinations = {} 

    for n in range(len(routes)):
        r = points[routes[n][0]-1][0]
        c = points[routes[n][0]-1][1]
        curr_positions[n] = [r, c]
        destinations[n] = 1

    while robots>1:
        now_positions = defaultdict(int) #r_c:int
        for n in range(len(routes)):
            if curr_positions[n]:
                r = curr_positions[n][0]
                c = curr_positions[n][1]
                now_positions[f"{r}_{c}"]+=1

        for position in now_positions:
            if now_positions[position]>1:
                answer+=1

        for n in range(len(routes)):
            if destinations[n]:
                destination_r = points[routes[n][destinations[n]]-1][0]
                destination_c = points[routes[n][destinations[n]]-1][1]
                r = curr_positions[n][0]
                c = curr_positions[n][1]

                if curr_positions[n][0] == destination_r and curr_positions[n][1] == destination_c:
                    if destinations[n]>=len(routes[n])-1:
                        robots-=1
                        destinations[n]=None
                        curr_positions[n] = None
                    else:
                        destinations[n]+=1
                        destination_r = points[routes[n][destinations[n]]-1][0]
                        destination_c = points[routes[n][destinations[n]]-1][1]

                if curr_positions[n]:
                    if r < destination_r:
                        curr_positions[n][0]+=1
                    elif r > destination_r:
                        curr_positions[n][0]-=1
                    elif c < destination_c:
                        curr_positions[n][1]+=1
                    elif c > destination_c:
                        curr_positions[n][1]-=1
            else:
                curr_positions[n] = None
    return answer