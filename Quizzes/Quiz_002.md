# Quiz 2
## Python code
```python
import time

def ipmachine1(x):
    ips  = []
    for a in range(x+1):
        for b in range(x+1):
            for c in range(x+1):
                for d in range(x+1):
                    ips.append(f"{a}.{b}.{c}.{d}")
    return ips

def ipmachine2(x):
    a = 0
    b = 0
    c = 0
    n = 0
    ls = []
    while True:
        d = n%x+1
        ls.append(f"{a}.{b}.{c}.{d}")
        #print(f"{a}.{b}.{c}.{d}")
        if d == x:
            c += 1
            if c == x+1:
                b += 1
                c = 0
                if b == x+1:
                    a += 1
                    b = 0
                    if a == x+1:
                        break
        n += 1
    return ls

def measureFunctionst():
    start = time.time()
    ipmachine1(40)
    end = time.time()
    print(end - start)
    start = time.time()
    ipmachine2(40)
    end = time.time()
    print(end - start)
```
## Output
![](/assets/Q_2.1.png)
![](/assets/Q_2.2.png)

## Flowchart
![](/flowCharts/ipmachine2.png)
