T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = []
    garo = []
    for i in range(N):
        data = input()
        garo.append(data)
        for k in range(len(data)-M+1):
            if data[k:M+k] == data[k:M+k][::-1]:
                result.append(data[k:M+k])

    sero =[]
    sero_particle = ''
    for x in range(N):
        for y in garo:
            sero_particle += y[x]
            sero_particle = ''
        sero.append(sero_particle)

    for sero_data in sero:
        for j in range(len(data)-M+1):
            if sero_data[j:M+j] == data[j:M+j][::-1]:
                result.append(sero_data[j:M+j])

    print("#%d %s"%(test_case, result[0]))








