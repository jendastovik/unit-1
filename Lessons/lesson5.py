word = "helllo world"
value = sum([ord(n) - 64 if n != " " else 0 for n in word.upper()])
print(value)

