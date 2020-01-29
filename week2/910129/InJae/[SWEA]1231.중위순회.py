def InorderTraveral(tree,i,N):
    if i<=N:
        InorderTraveral(tree,i*2,N)
        print(tree[i],end="")
        InorderTraveral(tree,i*2+1,N)

for t in range(1,11):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    for _ in range(N):
        inputValue = input().split(" ")
        node, item = inputValue[0:2]
        tree[int(node)] = item
    print("#{}".format(t),end = " ")
    InorderTraveral(tree,1,N)
    print("")


