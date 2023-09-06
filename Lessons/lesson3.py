import random

def largerInteger(A: int, B: int) -> int:
    if A > B:
        return A
    else:
        return B
    
def randomHexadecimal() -> str:
    """
    returns a random 4 digit hexadecimal number
    """
    hex = ""
    nums = "0123456789ABCDEF"
    for i in range(4):
        hex += nums[random.randint(0, len(nums)) - 1]
    return hex

def creatIPv6():
    IP = ""
    for j in range(8):
        hex = randomHexadecimal()
        IP += hex
        if j != 7:
            IP += ":"
    return IP

    
def  ipv6Machine(N: int) -> str:
    """
    returns random N ipv6 addresses
    """
    IPs = []
    for i in range(N):
        for j in range(100):
            IP = creatIPv6()
            if IP not in IPs:
                break
        IPs.append(IP)
    return IPs

def q3(N:int):
    """
    returns random N ipv6 addresses
    """
    IPs = []
    for i in range(N):
        for j in range(100):
            IP = ""
            for j in range(8):
                hex = randomHexadecimal()
                IP += hex
                if j != 7:
                    IP += ":"
            if IP not in IPs:
                    break
        IPs.append(IP)
    return IPs
    
#print(ipv6Machine(10))

N = 10
IPs = [":".join(["".join(["0123456789ABCDEF"[random.randint(0, 15)] for _ in range(4)]) for p in range(8)]) for i in range(N)]
print(IPs)


