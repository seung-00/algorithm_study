
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(10):
    tc = int(input())
    result = []
    data = []
    for i in range(100):
        lines = list(map(int, input().split()))
        data.append(lines)

    # 행의 합들을 구한다.

    for y in range(100):
        row = 0
        for x in range(100):
            row += data[y][x]

        result.append(row)

    # 열의 합을 구한다.

    for x in range(100):
        col = 0
        for y in range(100):
            col += data[y][x]
        result.append(col)

    # 대각선의 합을 구한다
    dae1, dae2 = 0, 0
    for y in range(100):
        dae1 += data[y][y]
        dae2 += data[y][100-y-1]

    result.insert(dae1, dae2)

    print("#{} {}".format(tc, max(result)))





