TC = int(input())
arr = [i for i in range(1,13)]
for case in range(TC):
    rst = []
    cnt = 0
    n = len(arr)
    subsetNum, subsetSum = map(int,input().split())
    for i in range(1<<n):	#1<<n: 부분 집합의 개수
        try:
            for j in range(n):	#원소의 수만큼 비트를 비교함
                if i&(1<<j):		#i의 j번째 비트가 1이면 j번째 원소
                    rst.append(arr[j])
                if(len(rst) > subsetNum):
                    raise Exception    #제한된 부분 집합 길이보다 길어지면 예외 처리
            if(len(rst)==subsetNum and sum(rst) == subsetSum):
                cnt += 1
        except Exception as e:
            pass
        rst.clear()
    print("#{} {}".format(case+1, cnt))