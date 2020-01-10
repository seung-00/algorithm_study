
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    result = [0]*num
    data = list(map(int, input().split()))
    for i in range(num//2):
        result[i*2] = max(data)
        data.pop(data.index(max(data)))
    for i in range(num//2):
        result[i*2 + 1] = min(data)
        data.pop(data.index(min(data)))

    print("#%s"%test_case,end = " ")
    for i in range(10):
        print(result[i], end = " ")
    print()


