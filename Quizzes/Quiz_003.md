# Quiz 3
## Python code
```python
def ipV6Machine(N):
    IPs = [":".join(["".join(["0123456789ABCDEF"[random.randint(0, 15)] for _ in range(4)]) for p in range(8)]) for i in range(N)]
    return IPs
```