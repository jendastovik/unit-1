def door_flipper(N):
    doors = [False] * N
    for stu in range(N):
        for d in range(stu, N, stu+1):
            doors[d] = not doors[d]
    return doors
