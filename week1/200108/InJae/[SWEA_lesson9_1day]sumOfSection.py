test = int(input())
rst_list = []
for _ in range(test):
    N,M = map(int,input().split())
    num_list = list(map(int,input().split()))


    sum_value=sum(num_list[:M])
    sum_list = [sum_value]
    for i in range(N-M):
        sum_value = sum_value-num_list[i]+num_list[M+i]
        sum_list.append(sum_value)

    rst_list.append(max(sum_list)-min(sum_list))

for t,rst in enumerate(rst_list):
    print("#{} {}".format(t,rst))
