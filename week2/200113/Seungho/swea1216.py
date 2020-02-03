
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    T = int(input())
    result = 1
    garo = []
    for i in range(100):
        data = input()
        garo.append(data)
        for M in range(100, 1, -1):
            for k in range(100-M+1):
                if data[k:M+k] == data[k:M+k][::-1] and result < len(data[k:M+k]):
                    result = len(data[k:M+k])


    sero =[]
    for x in range(100):
        sero_particle = ''
        for y in garo:
            sero_particle += y[x]

        sero.append(sero_particle)

    for sero_data in sero:
        for M in range(100, 1, -1):
            for k in range(100-M+1):
                if sero_data[k:M+k] == sero_data[k:M+k][::-1] and result < len(sero_data[k:M+k]):
                    result = len(sero_data[k:M+k])


    print("#{} {}".format(T, result))








