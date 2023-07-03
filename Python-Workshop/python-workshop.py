# exercise 1

with open("/Users/justinconn/Projects/NZMSA-Workshop/Python-Workshop/transmissions.csv") as file:
    transmisionsLst = [line.strip().split(",") for line in file]

# print(transmisionsLst)

# exercise 2
transmisionsLst.pop(0)
sumsLst = []
for lst in transmisionsLst:
    sums = 0
    for i in lst[1]:
        try:
            sums += int(i)
        except:
            continue
    sumsLst.append(sums)

# print(sumsLst)

# exercise 3
myDict = {}
for lst in transmisionsLst:
    myDict[int(lst[0])] = sumsLst.pop(0)

sentence = [chr(myDict[key]) for key in sorted(myDict)]
print("".join(sentence))