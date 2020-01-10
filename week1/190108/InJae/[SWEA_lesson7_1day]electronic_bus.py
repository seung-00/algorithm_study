test = int(input())

rst_list = []

def FindValue(K,N,list_loc_charging):
    rst = 0
    min_charging = 101

    def DFS(K, N, loc_cur, cnt, list_loc_charing):
        if N-loc_cur <= K:
            nonlocal min_charging
            if min_charging > cnt:
                min_charging = cnt
            return

        else:
            for i in range(1, K + 1):
                if list_loc_charging[loc_cur + i] == True:
                    DFS(K, N, loc_cur + i, cnt + 1, list_loc_charging)

    DFS(K, N, 0, 0, list_loc_charging)

    if min_charging == 101:
        rst = 0

    else:
        rst = min_charging

    return rst


for _ in range(test):
    #input값 받기
    K,N,M = map(int,input().split())
    M_list = list(map(int,input().split()))

    #list_loc_charging(정류소 있는지 위치확인해주는 값)에 충전소가 있으면 True없으면 False 입력해주는 과정
    list_loc_charging = [False] * (N + 1)
    for i_M in M_list:
        list_loc_charging[i_M] = True

    #값 구하기
    rst_list.append(FindValue(K,N,list_loc_charging))

for t,rst in enumerate(rst_list):
    print("#{} {}".format(t+1,rst))
