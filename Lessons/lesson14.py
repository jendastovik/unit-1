def blackBox3(sen):
    sen = sen.lower()
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

print("hello world -> " + blackBox3("hello world"))
print("aaaaAABB -> " + blackBox3("aaaaAABB"))
print("abABabAB -> " + blackBox3("abABabAB"))
print("Create a Function -> " + blackBox3("Create a Function"))