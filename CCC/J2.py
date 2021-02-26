bidders = int(input())
x = []
y = []
for i in range(bidders):
    x.append(input())
    y.append(int(input()))
highestprice = y.index(max(y))

print(x[highestprice])
