# Quiz 15

## Python code
```python
def door_flipper(N):
    doors = [False] * N
    for stu in range(N):
        for d in range(stu, N, stu+1):
            doors[d] = not doors[d]
    return doors
```

## Output
![](/assets/Q_15.png)

## Flowchart
![](/flowCharts/q15.png)
