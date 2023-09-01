word = "hello world"
def val(word):
    value = sum([ord(n) - 64 if n != " " else 0 for n in word.upper()])
    return value
print("hello world -> " + str(val(word)))
print("hello -> " + str(val("hello")))
print("world -> " + str(val("world")))

