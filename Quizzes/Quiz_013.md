# Quiz 14

## Python code
```python
def blackBox3(sen):
    out = ""
    used = {}
    for l in sen:
        if l == " ":
            out += " "
            continue
        elif l in used:
            used[l] += 1
        else:
            used[l] = 1
        out += str(used[l])
    return out
```

## Output
![](/assets/Q_13.png)

## Flowchart
![](/flowCharts/q13.png)
