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
count = 0
for lst in transmisionsLst:
    sumsLst[count] = [int(lst[0]), sumsLst[count]]
    count += 1

sortLst = sorted(sumsLst, key=lambda x:x[0])

sentence = ""
for i in sortLst:
    sentence += (chr(i[1]))

print(sentence)