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

print(blackBox3("hello world"))
print(blackBox3("aAbBaA"))