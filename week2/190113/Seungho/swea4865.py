T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    max_count , sub_count = 0,0
    for i in str1:
        for j in str2:
            if i == j:
                sub_count += 1
        if max_count < sub_count:
            max_count = sub_count

        sub_count = 0

    print("#{} {}".format(test_case, max_count))


