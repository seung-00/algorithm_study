test = int(input())
rstList = []
def Sol(startV,G,grape):
    rst = 0
    def DFS(startV,G,grape):
        if startV == G:
            nonlocal rst
            rst = 1
            return
        else:
            for v in grape[startV]:
                DFS(v,G,grape)
    DFS(startV,G,grape)
    return rst

for _ in range(test):
    V,E = map(int,input().split())
    grape = [[] for _ in range(V+1)] #V가 1번부터 주어짐. 연속된 번호로 주어진다고 보자.

    for _ in range(E): #간선 정보만큼 입력받음.
        startV, endV = map(int,input().split())
        grape[startV].append(endV) #startV->endV 방향성 그래프이므로 index -> 출발노드, value는 갈 수 있는 노드로 봄.

    S,G = map(int,(input().split()))
    rst = Sol(S,G,grape)

    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))
