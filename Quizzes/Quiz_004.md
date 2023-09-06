# Quiz 4
## Python code
```python
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

def PerfecDeviders(N):
    dev = [i for i in range(1, N) if N%i == 0]
    return dev
```
## Output
![](/assets/Q_4.1.png)
![](/assets/Q_4.2.png) 

## Flowchart
![](/flowCharts/q4.png)

