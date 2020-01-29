cases = 10
for case in range(cases):
    length = int(input())
    buildings = list(map(int, input().split()))
    cnt = length - 4
    views = []
    for i in range(cnt):
        heights = buildings[i:i+5]
        minView = heights[2] #height of viewer
        for j in range(len(heights)):
            if(j == 2): continue
            tempView = heights[2]-heights[j]
            if(minView>tempView and tempView >= 0):
                minView = tempView
            elif(tempView<0):
                minView = 0
                break
        views.append(minView)
    print("#{} {}".format(case+1,sum(views)))