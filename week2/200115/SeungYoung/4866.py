def Func():
    stack = []
    line = list(map(str, input()))
    for i in line:
        if i == '(' or i == '{':
            stack.append(i)
        else:
            if i == ')':
                if len(stack) == 0:
                    return 0
                elif stack.pop() != '(':
                    return 0
            elif i == '}':
                if len(stack) == 0:
                    return 0
                elif stack.pop() != '{':
                    return 0
                
    if len(stack) != 0:
        return 0
    return 1

tc = int(input())
for case in range(tc):
    print("#{} {}".format(case+1, Func()))