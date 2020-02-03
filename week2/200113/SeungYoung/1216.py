def GetTrans(matrix):
    return [list(i) for i in zip(*matrix)]

#재귀로 구현 
def IsPalindrome(string):
    # for i in range(len(string)//2):
    #     if(string[i]!=string[len(string)-1-i]):
    #         return False
    # return True 
    if len(string) <2:
        return True
    if string[0]!=string[-1]:
        return False
    return IsPalindrome(string[1:-1])


TC = 10
for case in range(TC):
    thisCase = int(input())
    maxLen = 1
    matrix = []
    rowLen, colLen = 100, 100
    for i in range(rowLen):
        row = list(map(str,input()))
        matrix.append(row)
    for line in matrix:
        for subsetLen in range(colLen, 2, -1): #길이가 1인 건 확인할 필요가 없다.
            if subsetLen<maxLen: #maxLen보다 짧은 부분집한은 체크할 필요가 없다.
                break
            for idx in range(len(line)-subsetLen+1):    #부분집합은 0 - len(line)-subsetLine까지가 리스트의 시작 지점
                if IsPalindrome(line[idx:idx+subsetLen]):
                    maxLen = subsetLen
                    break
    
# 열 비교
    for line in GetTrans(matrix):
        for subsetLen in range(colLen, maxLen, -1):  #maxLen보다 짧은 열은 체크할 필요가 없다.
            if subsetLen<maxLen: 
                break
            for idx in range(len(line)-subsetLen+1):    #부분집합은 0 - len(line)-subsetLine까지가 리스트의 시작 지점
                if IsPalindrome(line[idx:idx+subsetLen]):
                    maxLen = subsetLen
                    break
    print("#{} {}".format(thisCase, maxLen))