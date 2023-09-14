# Quiz 11

## Python code
```python
def reverse1(string:str) -> str:
    return string[::-1]

def reverse2(string:str) -> str:
    output = ""
    if len(string)%2 == 1:
        mid = len(string)//2
        output += string[mid]
        for i in range(mid):
            output = string[mid+i+1] + output + string[mid-i-1]
    else:
        mid = len(string)//2
        for i in range(mid):
            output = string[mid+i] + output + string[mid-i-1]
    return output

def reverse3(string:str) -> str:
    output = ""
    for i in string:
        output = i + output
    return output

def reverse4(string:str) -> str:
    output = ""
    for i in range(len(string), 0, -1):
        output += string[i-1]
    return output
    

def reverse5(string:str) -> str:
    output = ""
    ls = [let for let in string]
    ls.reverse()
    output = "".join(ls)
    return output

def reverse6(string:str) -> str:
    output = ""
    ls = [""]*len(string)
    for i in range(len(string)):
        ls[abs(i-len(string)+1)] = string[i]
    output = "".join(ls)
    return output
```

## Output
![](/assets/Q_11.png)

## Flowchart
![](/flowCharts/q11.png)