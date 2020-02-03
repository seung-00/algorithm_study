def BruteForce(pattern, txt):
    i = 0		#txt의 인덱스
    j = 0		#pattern의 인덱스
    M = len(pattern)
    N = len(txt)
    while j < M and i < N:
        if txt[i] != pattern[j]:
            i = i - j #j 만큼 앞으로 갔던거 다시 뺵
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return True # 검색 성공
    else: return False	#검색 실패

TC = 1
#int(input())
for case in range(TC):
    pattern = input()
    txt = input()
    if(BruteForce(pattern, txt)):   print("#{} {}".format(case+1, 1))
    else:   print("#{} {}".format(case+1, 0))