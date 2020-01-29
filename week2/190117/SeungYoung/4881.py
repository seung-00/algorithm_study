def DFS(table, row, score, col_check):
    minScore = 100000
    def Func(table, row, score, col_check):
        nonlocal minScore
        if score > minScore:
            return minScore
            
        elif row == len(table):
            if score<minScore:
                minScore = score
            return minScore

        for i in range(len(table)):
            if not col_check[i]:
                col_check[i] = True
                Func(table, row+1, score+table[row][i], col_check)
                col_check[i] = False    # call by ref
        return minScore
    return Func(table, row, score, col_check)


tc = int(input())
answers = []



for c in range(tc):
    tableLen = int(input())
    table = [list(map(int, input().split())) for _ in range(tableLen)]
    col_check = [False for i in range(len(table))]
    answers.append(DFS(table, 0, 0, col_check))

for t, answer in enumerate(answers):
    print("#{} {}".format(t+1, answer))