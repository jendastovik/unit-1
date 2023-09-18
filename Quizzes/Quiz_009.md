# Quiz 9

## Python code
```python
def un(N):
    units = ["pico", "nano", "micro", "milli", "unit", "kilo", "mega", "giga", "tera"]
    units.reverse()
    powers = [12, 9, 6, 3, 0, -3, -6, -9, -12]
    output = ""
    for rep in range(len(units)):
        output += (f"{N*10**powers[rep]} {units[rep]}" + "\n")

    return output
```

## Output
![](/assets/Q_9.png)

## Flowchart
![](/flowCharts/q9.png)