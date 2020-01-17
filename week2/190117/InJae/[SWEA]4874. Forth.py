class STACK:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return False

    def push(self,a):
        self.stack.append(a)

    def isempty(self):
        if self.stack:
            return False
        else:
            return True

def Ccl(a,b,op):
    if op == '/':
        return str(int(a)//int(b))
    return eval(a+op+b)

test = int(input())
rstList = []
for t in range(test):
    stringList = list(map(str,input().split()))
    stack = STACK()
    flag = True
    ac = 0
    for s in stringList:
        if s.isnumeric():
            stack.push(s)
        elif s == '.':
            ac = int(stack.pop())
            if not stack.isempty():
                flag = False
            break

        else:
            op = s
            a = stack.pop()
            b = stack.pop()

            if a and b:
                stack.push(str(Ccl(b,a,op)))
            else:
                flag = False
                break

    if flag:
        rst = ac
    else:
        rst = 'error'


    print("#{} {}".format(t+1,rst))
    #rstList.append(rst)

#for t,rst in enumerate(rstList):
#    print("#{} {}".format(t+1,rst))