class NODE:
    def __init__(self):
        self.left = self.right = None

def CountDsdtNodes(N):
    cnt = 1 #root노트도 포함
    def _CountDsdtNodes(N): # input : descendent수를 찾고자하는 노드의 번호   output : descendent의 수
        nonlocal cnt
        if parentChildList[N].left is not None:
            cnt += 1
            _CountDsdtNodes(parentChildList[N].left)
        if parentChildList[N].right is not None:
            cnt += 1
            _CountDsdtNodes(parentChildList[N].right)
    _CountDsdtNodes(N)
    return cnt

test = int(input())
rstList = []

for _ in range(test):
    rst = 0
    E,N = map(int,input().split())
    parentChildList = [NODE() for _ in range(E+2)]
    inputValues = list(map(int,input().split()))
    idxParent = 0 # 정렬에서 인덱스 참조 응용해보기!
    idxChild = 1
    endCase = E*2
    while idxParent != endCase:
        parentValue = inputValues[idxParent]
        childValue = inputValues[idxChild]
        if parentChildList[parentValue].left is None:
            parentChildList[parentValue].left = childValue
        else:
            parentChildList[parentValue].right = childValue
        idxParent += 2
        idxChild += 2

    rst = CountDsdtNodes(N)
    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))