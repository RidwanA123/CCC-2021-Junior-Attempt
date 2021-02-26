from sys import stdin
columes = int(stdin.readline())
rows = int(stdin.readline())
instances = int(stdin.readline())

counter = 0
ins = []
for i in range(instances):
    ins.append(stdin.readline().split(" "))
arr = []
for i in range(columes):
    a = "B" * rows
    arr.append(list(map(str,a)))
for i in range(len(ins)):
    if ins[i][0] == "R":
        num = int(ins[i][1])
        for b in range(len(arr[num-1])):
            if arr[num-1][b-1] == "B":
                arr[num-1][b-1] = "G"
            else:
                arr[num-1][b-1] = "B"
    else:
        num = int(ins[i][1])
        for b in range(len(arr)):
            if arr[b-1][num-1] == "B":
                arr[b-1][num-1] = "G"
            else:
                arr[b-1][num-1] = "B"
for i in range(len(arr)):
    for b in range(len(arr[i-1])):
        if arr[i-1][b-1] == "G":
            counter = counter + 1
print(counter)
               
