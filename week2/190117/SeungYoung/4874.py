TC = int(input())

for tc in range(1, TC+1):
    data = list(input().split())
    N = len(data)
    stack = []
    flag = 0

    # 마침표는 제외하기 위해 N-1까지 반복
    for i in range(N-1):  
        # 피연산자 push
        if data[i].isdigit():
            stack.append(data[i])

        else:
            try:  # 후위표기 계산
                num2, num1 = int(stack.pop()), int(stack.pop())

                if data[i] == "+": result = num1 + num2
                elif data[i] == "-": result = num1 - num2
                elif data[i] == "/": result = num1 // num2
                elif data[i] == "*": result = num1 * num2

                stack.append(str(result))

            except: # ex 숫자 + 연산자 + 연산자
                flag = 999

    #예외처리 조건 (X) + Stack의 길이가 1인 경우(계산이 성공적인경우)
    if flag == 0 and len(stack) == 1:
        print('#{} {}'.format(tc, stack.pop()))

    #예외처리 조건 (O) + stack의 길이가 2이상인 경우 ex) 숫자만 입력된 경우
    elif flag == 999 or len(stack)>1:
        print('#{} {}'.format(tc, 'error'))
