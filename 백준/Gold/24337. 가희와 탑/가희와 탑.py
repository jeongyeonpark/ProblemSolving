def main(N, a, b):
    result = []
    for k in range(N-a-b+1):
        result.append(str(1))
        N -= 1
    if a >= b:
        add_result, N = run(a, b, N)
    else:
        add_result, N = run(b, a, N)
        add_result.reverse()

    if a ==1:
        print((add_result[0]+ " " + " ".join(result) + " " + " ".join(add_result[1:]) if result else " ".join(add_result)) if N == 0 else -1)
    else:
        print((" ".join(result) + " " + " ".join(add_result) if result else " ".join(add_result)) if N == 0 else -1)
    
def run(x, y, N):
    add_result = []
    for i in range(x):
        add_result.append(str(i + 1))
        N -= 1
    for j in range(y -2, -1, -1):
        add_result.append(str(j + 1))
        N -= 1
    
    return add_result, N

if __name__ == "__main__":
    N, a, b = map(int, input().split())

    main(N, a, b)