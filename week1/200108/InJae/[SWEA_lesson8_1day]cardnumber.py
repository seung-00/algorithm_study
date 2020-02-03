test = int(input())

for t in range(test):
    n_cards = int(input())
    cards=input()

    counts = [0]*10

    for card in cards:
        counts[int(card)]+=1

    cnt_max = -1
    num_in_cnt_max=-1

    for number,count in enumerate(counts):
        if cnt_max<count:
            cnt_max = count
            num_in_cnt_max = number

        elif cnt_max == count:
            if number > num_in_cnt_max:
                cnt_max = count
                num_in_cnt_max = number

    print("#{} {} {}".format(t+1,num_in_cnt_max,cnt_max))