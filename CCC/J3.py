main = []
prev = ""
arr1 = []
while True:
    x = input()
    if x == "99999":
        break
    else:
        main.append(x)
for i in range(len(main)):
    temp = main[i]
    arr1 = list(map(str,temp))
    tens = []
    compare = []
    tens.append(str(arr1[0]))
    tens.append(str(arr1[1]))
    compare.append(str(arr1[2]))
    compare.append(str(arr1[3]))
    compare.append(str(arr1[4]))
    if ((int(tens[0]) == 0) and (int(tens[0]) == 0)):
        print(prev+" "+compare[0]+compare[1]+compare[2])

    elif ((int(tens[0]) + int(tens[1])) % 2 == 0):
        print("right "+compare[0]+compare[1]+compare[2])
        prev = "right"
    elif ((int(tens[0]) + int(tens[1])) % 2 != 0):
        print("left "+compare[0]+compare[1]+compare[2])
        prev = "left"
    
