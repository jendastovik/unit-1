import random

class generator:
    def __init__(self, N) -> None:
        self.N = N

    def randomMacGenerator(self):
        """
        creates n different random mac adresses
        """
        MACs = []
        while len(MACs) != self.N:
            num = str(hex(random.randint(0, 281474976710655)))
            while len(num) != 14:
                num  = "0" + num
            for p in range(2, 6*3, 3):
                num = num[:p] + ":" + num[p:]
            num = num[3:]
            if num not in MACs:
                MACs.append(num)
        return MACs
    
gen = generator(10)
#print(gen.randomMacGenerator())

N = 90
ls = [i for i in range(1, N) if N%i == 0]
print(ls)
