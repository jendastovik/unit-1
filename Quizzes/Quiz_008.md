# Quiz 8

## Python code
```python
def cipher(word:str, N):
    if N<0: 
        N = 26 + N
    new = ""
    for l in word:
        if l ==" ":
            new += l
        elif ord(l)+N<=ord("z"):
            new += chr(ord(l) + 13)
        else: 
            new += chr(ord("a") + ord(l)+N-1-ord("z"))
    return new
```

## Output
![](/assets/Q_8.png)

## Flowchart
![](/flowCharts/q8.png)