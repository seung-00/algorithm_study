T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
A = [1,2,3,4,5,6,7,8,9,10,11,12]
A_lenght = len(A)
num_set = []
# 부분집합들의 리스트
for i in range(1<<A_lenght):
    subset = []
    result = 0
    for j in range(A_lenght):
        if(i&(1<<j)):
            subset.append(A[j])
    num_set.append(subset)


for test_case in range(1, T + 1):
    N,K = map(int, input().split())
    N_list = []
    for i in num_set:
        if len(i) == N:
            N_list.append(i)

    for i in N_list:
        if sum(i) == K:
            result += 1

    print("#{} {}".format(test_case, result))
