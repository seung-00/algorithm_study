
T = int(input())
for test_case in range(1, T + 1):
    Searchinfo = list(map(int, input().split()))
    result = []
    for j in range(2):
        start = 1
        end = Searchinfo[0]
        page = Searchinfo[j+1]
        count = 0

        while start < end:
            mid = (start + end)//2

            if mid == page:
                break

            elif mid < page:
                start = mid
                count +=1

            else :
                end = mid
                count +=1
        result.append(count)

    if result[0] > result[1]:
        print("#{} {}".format(test_case,"B"))

    elif result[0] < result[1]:
        print("#{} {}".format(test_case, "A"))
    else :
        print("#{} 0".format(test_case))

            



    

        
    
        

