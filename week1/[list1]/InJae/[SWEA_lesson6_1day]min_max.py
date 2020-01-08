def BubbleSort(input_list):     #input : list , output= sorted_list
    for i in range(len(input_list)-1,-1,-1):
        for j in range(0,i):
            if input_list[j]>input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp

    return input_list


n_test = int(input())
rst_list = []

for _ in range(n_test):
    n_my_list = int(input())
    my_list = list(map(int,input().split()))
    sorted_my_list = BubbleSort(my_list)
    rst_list.append(sorted_my_list[n_my_list-1]-sorted_my_list[0])

for t,rst_list in enumerate(rst_list):
    print("#{} {}".format(t+1,rst_list))