import heapq

#가장 첫 줄은 전체 테스트 케이스의 수이다.
tc = int(input())

for c in range(tc):
    #각 테스트 케이스는 정수 K 하나가 쓰여진 줄 다음에 영어 소문자로 된 문자열이 쓰인 줄로 이루어진다.
    K = int(input())
    text = input()
    if K > len(text):
        print(f"#{c+1} none")
        continue
    strTails = []
    for i in range(len(text)):
        heapq.heappush(strTails, text[i:])
#    strTails = sorted(strTails)
    
#    print(f"#{c+1} {strTails[K-1]}")
    print(strTails)
