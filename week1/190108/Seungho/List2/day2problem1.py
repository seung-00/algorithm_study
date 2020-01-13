T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    Matrix = [[0]*5 for i in range(5)]
    red = []
    blue = []
    purple = []
    for i in range(N):
        y1, x1, y2, x2, color = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if color == 1:
                    red.append((y, x))
                else:
                    blue.append((y, x))
    
    if len(red) > len(blue):
        for i in blue:
            if i in red:
                purple.append(i)
    else :
        for i in red:
            if i in blue:
                purple.append(i)
                
    print("#{} {}".format(test_case, len(purple)))


        
        

