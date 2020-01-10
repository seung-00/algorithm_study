def Dump(dumpCnt, boxes):
    for i in range(dumpCnt):
        boxes = sorted(boxes)
        if(boxes[len(boxes)-1] - boxes[0] < 2):
            return boxes[len(boxes)-1]-boxes[0]
        else:
            boxes[len(boxes)-1]-=1
            boxes[0]+=1
        boxes = sorted(boxes)
    return boxes[len(boxes)-1] - boxes[0]

for i in range(10):
    dumpCnt = int(input())
    boxes = list(map(int, input().split()))
    answer = Dump(dumpCnt, boxes)
    print("#{} {}".format(i+1,answer))