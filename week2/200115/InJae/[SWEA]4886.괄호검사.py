rstList = []
test = int(input())
for _ in range(test):
    stack = []
    string = input()
    rst = 0
    overFlag = False #중간에 pop이 잘못됬는지 판단
    for s in string:
        ### 소괄호가 들어올 경우
        if s == '(':
            stack.append('(')
        elif s == ')':
            if stack: #stack 에 값이 있는 경우
                if stack[-1] == '(':
                    stack.pop()
                else:
                    overFlag = True
                    break

            else: #stack에 값이 없는 경우
                overFlag = True
                break

        elif s == '{':
            stack.append('{')

        elif s == '}':
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    overFlag = True
                    break
            else:
                overFlag = True
                break

    if overFlag : #중간에 끝났다는 걸 알려줘야함. 비어있는지만 판단해서는 잘못되서 비어있는건지, 다끝나서 비어있는건지 구분 안됨.
        rst  = 0
    else:
        if stack:
            rst = 0
        else:
            rst = 1

    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))
