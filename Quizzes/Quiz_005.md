# Quiz 5
## Python code
```python
def ValueSentence(sentence:str):
    value = sum([ord(n) - 64 if n != " " else 0 for n in sentence.upper()])
    return value
```
## Output
![](/assets/Q_5.png)