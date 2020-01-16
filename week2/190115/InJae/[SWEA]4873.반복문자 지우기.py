test = int(input())
rstList = []
class STACK:
    def __init__(self,n):
        self.stack = [0 for _ in range(n+1)]
        self.pointer = 0 #0값은 안씀 초기값 지정 pointer은 현재 값이 있는 위치 나타내줌 top이라 보면 됨.

    def push(self,s):
        self.pointer+=1
        self.stack[self.pointer] = s

    def pop(self):
        self.pointer -= 1

    def sol(self,s):
        if s == self.stack[self.pointer]:
            self.pop()
        else:
            self.push(s)

for _ in range(test):
    string = input()
    rst = 0
    stack = STACK(len(string))
    for s in string:
        stack.sol(s)

    rst = stack.pointer
    rstList.append(rst)
for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))
