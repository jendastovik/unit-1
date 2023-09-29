from numpy import average


words = ["computer science", "art"]
av = average([len(w) for w in words])
av2 = sum([len(w) for w in words]) / len(words)
print(av)


numbers = [1, 2, 3, 4, 5]

def averageLenght(words):
    return sum([len(w) for w in words]) / len(words)

print(f'computer science, art --> {averageLenght(["computer science", "art"])}')
print(f'computer science, art, science --> {averageLenght(["computer science", "art", "science"])}')
print(f'computer science, art, science, math --> {averageLenght(["computer science", "art", "science", "math"])}')
print(f'hello, main --> {averageLenght(["hello", "main"])}')


