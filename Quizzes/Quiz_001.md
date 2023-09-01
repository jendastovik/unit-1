# Quiz 1
## Python code
```python
def wordShortener(str1: str):
    spl = str1.split()
    final = ""
    for word in spl:
        if len(word) > 2:
            final += word[0] + str(len(word) - 2) + word[-1]
        else:
            final += word
        final += " "
    return final
```

## Output
![](/assets/Q_1.png) 

## Flowchart
![](/flowCharts/quizz1.png)

