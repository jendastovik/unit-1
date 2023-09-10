# Quiz 7

## Python code
```python
import random
def rand():
    con = True
    times = 0
    while con:
        n = random.randint(1, 100)
        times += 1
        if n <= 15:
            con = False
    return times
```

## Output
![](/assets/Q_7.png)

## Flowchart
![](/flowCharts/q7.png)
