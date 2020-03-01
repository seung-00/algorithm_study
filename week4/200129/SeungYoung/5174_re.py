class Node:
    def __init__(self,left=None,right=None,val=None):
        self.left = left
        self.right = right
        self.val = val

tc = int(input())
for case in range(1, tc+1):
    E, N = map(int, input().split())

    temp = list(map(int,input().split()))
    root = temp[0]

    graph = {p:[] for p in range(1,E+2)}

    for _ in range(E):
        p, c = temp.pop(0), temp.pop(0)
        graph[p].append(c)
#    print(graph)

    #BFS
    que = []
    que.append(N)
    cnt = 0
    while que:
        child = que.pop(0)
        cnt+=1
        que.extend(graph[child])
    print("#{} {}".format(case, cnt))