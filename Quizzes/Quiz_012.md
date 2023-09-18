# Quiz 12

## Python code
```python
def mystery(x, y):
    dif = x - y
    return (x*y + dif)

test_cases = [(2, 6), (4, 10), (10, 10), (70, 50)]
for (a, b) in test_cases:
    print(f"{a}, {b} ==> {mystery(a, b)}")
```

## Output
![](/assets/Q_12.png)

## Flowchart
![](/flowCharts/q12.png)
