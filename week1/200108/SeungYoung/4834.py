cases = int(input())
for case in range(cases):
    N = int(input())
    cards = input()
    counts = [0]*10
    for card in cards:
        counts[int(card)] = counts[int(card)]+1

    maxNum = 0
    cardNum = 0
    
    for i in range(len(counts)):
        if(counts[i] == maxNum and i > cardNum):
            cardNum = i
        elif(counts[i]>maxNum):
            cardNum = i
            maxNum = counts[i]
    print("#{} {} {}".format(case+1,cardNum, maxNum))