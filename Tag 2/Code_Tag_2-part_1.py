import string

f =  open("Tag 2/input.txt", "r")

list1 = []
list2 = []
list3 = []
list4 = []
müll = []
überspringen = []
enderbenis = 0

#Einlesen der Datei
for line in f:
    line = line.strip().split("\n")
    list1.append(line)
for i in range(len(list1)):
    bline = []
    for j in range(len(list1[i])):
        xline = list1[i][j].split(" ")
        bline.append(xline)
        if j == len(list1[i])-1:
            list2.append((i , bline))#i = Zugewiesene Zahl des Fehlercodes (bline = zugewiesene Fehler als Liste im Tupel)

#entfernen aller Listen bei denen eine Zahl doppelt ist
for i in range(len(list2)):
    for j in range(len(list2[i][1])):
        wertalt = int(0)
        spring = False
        firsttime = True
        firsttimeb = True
        for k in range(len(list2[i][1][j])):
            if list2[i][1][j][k] != wertalt and spring == False:
                spring = False
                wertalt = list2[i][1][j][k]
                if firsttimeb == True:
                    list3.append(list2[i][1][j])
                    firsttimeb = False
            else:
                spring = True
                if firsttime == True:
                    müll.append(list2[i][1][j])
                    firsttime = False
            if k == len(list2[i][1][j])-1 and spring == False:
                list4.append(list3)
                list3 = []
            elif k == len(list2[i][1][j])-1 and spring == True:
                list3 = []

#print(f"Müll: {müll}")
print(list4)
print("------------------------------------------------------------------------------------------------------------------------------")
print(f"Anzahl Ausschuss: {len(müll)} || Anzahl Liste 2: {len(list2)} || Anzahl Liste 3: {len(list3)} || Anzahl Liste 4: {len(list4)}")