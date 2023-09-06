word = "hello world"
def val(word):
    value = sum([ord(n) - 64 if n != " " else 0 for n in word.upper()])
    return value

print("hello world -> " + str(val(word)))
print("hello -> " + str(val("hello")))
print("world -> " + str(val("world")))
print("a -> " + str(val("m")))

def q5(word):
    sum = 0
    for n in word.upper():
        print(ord(n)-64, end=" ")
        if n != " ":
            sum += ord(n) - 64
        else:
            sum += 0
    return sum

print("math -> " + str(q5(word)))