def units(N):
    units = ["pico", "nano", "micro", "milli", "unit", "kilo", "mega", "giga", "tera"]
    p = 10**(-12)
    for i in range(len(units)):
        print(f"{N*p} {units[i]}")
        p = p*1000

#units(1)

def un(N):
    units = ["pico", "nano", "micro", "milli", "unit", "kilo", "mega", "giga", "tera"]
    units.reverse()
    powers = [12, 9, 6, 3, 0, -3, -6, -9, -12]
    output = ""
    for rep in range(len(units)):
        output += (f"{N*10**powers[rep]} {units[rep]}" + "\n")

    return output

print(un(1))