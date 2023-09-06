def ToBin(dec:int):
    bin = ""
    for k in range(7, -1, -1):
        if dec >= 2**k:
            dec -= 2**k
            bin += "1"
        else:
            bin += "0"
    return bin

print(f"10 -> {ToBin(10)}")
print(f"90 -> {ToBin(90)}")
print(f"255 -> {ToBin(255)}")

def AddBit(bin:str):
    if bin.count("1")%2==0:
            bin = "1" + bin
    else:
            bin = "0" + bin
    return bin

def CheckBin(bin:str):
     if bin[0] == "1" and bin[1:].count("1")%2 == 0:
          return True
     elif bin[0] == "0" and bin[1:].count("1")%2 == 1:
          return True
     else:
          return False
     
print(CheckBin(AddBit(ToBin(5))))
