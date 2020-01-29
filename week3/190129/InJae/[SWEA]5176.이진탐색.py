def SearchTree(n,nodeNum):
    global cnt
    if n <= nodeNum:
        SearchTree(n*2,nodeNum)
        tree[n] = cnt
        cnt+=1
        SearchTree(n*2+1,nodeNum)


rstList1 = []
rstList2 = []
test = int(input())

for _ in range(test):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    cnt = 1
    SearchTree(1,n)
    rstList1.append(tree[1])
    rstList2.append(tree[n//2])

for t in range(test):
    print("#{} {} {}".format(t+1,rstList1[t],rstList2[t]))



