
list = []
lorem_file = open("txtfile.txt", "r")
for line in lorem_file:
        for word in line.split():
           list.append(word)

print(list)

i = 0
n = 0
temp = ""
list2 = []
while i < len(list):
    temp = list[i]
    prot_gramma = temp[0]
    if len(temp) > 3:
        temp = temp.replace(prot_gramma, "")
        temp = temp + prot_gramma +"ay"
    list2.append(temp)
    i += 1
print("Meta alagi")
print(list2)


lorem_file.close()
