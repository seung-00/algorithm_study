test = int(input())
rstList = []

def FindWinner(s1,s2):
    if students[s1] == 1 and  students[s2] == 2:
        return s2
    elif students[s1] == 2 and  students[s2] == 1:
        return s1
    elif students[s1] == 2 and students[s2] == 3:
        return s2
    elif students[s1] == 3 and students[s2] == 2:
        return s1
    elif students[s1] == 1 and students[s2] == 3:
        return s1
    elif students[s1] == 3 and students[s2] == 1:
        return s2
    else:
        if s1<s2:
            return s1
        else:
            return s2

def Search(L,R):
    if R == L:
        return FindWinner(L,R)
    else:
        return FindWinner(Search(L,(L+R)//2),Search((L+R)//2+1,R))


for _ in range(test):
    N = int(input())
    students = list(map(int,input().split()))
    rst = Search(0,N-1) + 1
    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))
