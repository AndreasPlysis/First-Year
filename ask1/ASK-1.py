list = []
lorem_file = open("txtfile.txt", "r")
for line in lorem_file:
        for word in line.split():
           list.append(word)

print(list)
print("Meta to sort ")
list = sorted(list, key=len)
print(list)

i = 0
list2 = []
while i < 5:
    list2.append(list[-i-1])
    i += 1
print("5 pio megales leksis")
print(list2)

i = 0
temp = ""
list3 = []
while i < 5:
    temp = list2[i]
    fonien = ('a', 'e', 'i', 'o', 'u')
    for x in temp.lower():
        if x in fonien:
            temp = temp.replace(x, "")
    list3.append(temp)
    i += 1
print("Xoris fonienta")
print(list3)


print("Anapoda\n")
i = 0
temp = ""
while i < 5:
    temp = list3[i] [::-1]
    print(temp)
    i += 1

lorem_file.close()
