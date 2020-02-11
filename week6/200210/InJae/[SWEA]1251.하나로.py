test = int(input())
def CclDist(x1,y1,x2,y2):
    return ((x1-x2)**2+ (y1-y2)**2)**(1/2)
def prim()
for t in range(1,test+1):
    n = int(input())
    nodes = [tuple(map(int,input().split())) for _ in range(n)]
    distRC = {}
    for i in range(n):
        for j in range(n):
            distRC[(nodes[i],nodes[j])] = Ccl(nodes[i][0],nodes[i][1],nodes[j][0],nodes[j][1])

    nodeIdxs = list(range(n))
    selectRout = []