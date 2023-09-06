# Quiz 6

## Python code
```python
def ToBin(dec:int):
    bin = ""
    for k in range(7, -1, -1):
        if dec >= 2**k:
            dec -= 2**k
            bin += "1"
        else:
            bin += "0"
    return bin
```

## Output
![](/assets/Q_6.1.png)