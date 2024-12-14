import string

f =  open("Tag 1/input.txt", "r")

list1 = []
list2 = []
for line in f:
    line = line.strip().split("   ")
    list1.append(int(line[0]))
    list2.append(int(line[1]))
lista = sorted(list1)
listb = sorted(list2)

print(listb)
print(lista)