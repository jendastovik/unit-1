# Quiz 10

## Python code
```python
#version 1
def bestMonth():
    out = ""
    out += "November 2023"
    days = ["We", "Th", "Fr", "Sa", "Su", "Mo", "Tu"]
    for d in range(30):
        out += f", {days[d%7]} {d+1}"
    return out

#version 2
def calendar(offset):
    out = ""
    out += "November 2023"
    out += "\nMo Tu We Th Fr Sa Su\n"
    for _ in range(offset):
        out += "   "
    for d in range(30):
        if (d+offset)%7 == 0:
            out += "\n"
        out += f"{d+1:<2} "
    return out
```

## Output
![](/assets/Q_10.png)

## Flowchart
![](/flowCharts/q10.png)