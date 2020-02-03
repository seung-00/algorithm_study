T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            result = 1

    print("#{} {}".format(test_case, result))

