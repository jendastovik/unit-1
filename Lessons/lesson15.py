def door_flipper(N):
    doors = [False] * N
    for stu in range(N):
        for d in range(stu, N, stu+1):
            doors[d] = not doors[d]
    return doors

def ran(L, N):
    for _ in range(L):
        N = N // L
    if N == 0 or L%2 == 1:
        return (L, L%2 == 1)
    else:
        return (N, True)

def run_ran(N, L):
    print(f"{L} {N} --> {ran(L,N)}")

run_ran(999, 5)
