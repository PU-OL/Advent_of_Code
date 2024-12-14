import string

f =  open("Tag 1/input.txt", "r")

list1 = []
list2 = []
vorhanden = []
test = []
add = []
count = 0
enderbenis = 0
for line in f:
    line = line.strip().split("   ")
    list1.append(int(line[0]))
    list2.append(int(line[1]))
lista = sorted(list1)
listb = sorted(list2)
for i in range(len(lista)):
    if lista[i] != vorhanden:
        vorhanden.append(lista[i])

for j in range(len(vorhanden)):
    for i in range(len(listb)):
        if listb[i] == vorhanden[j]:
            count +=1
        if i == len(listb)-1 and count != 0:
            test.append((vorhanden[j], count))
            count = 0
for i in range(len(test)):
    multi = test[0][i] * test[1][i]
    add.append[multi]
for i in range(len(add)):
    