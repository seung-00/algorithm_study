cases = int(input())
for case in range(cases):
	nums = int(input())
	strNums = input()
	tempList = strNums.split()
	for i in range(nums):
		tempList[i] = int(tempList[i])
	tempList = sorted(tempList)
	print("#"+str(case+1), end=" ")
	print(tempList[nums-1] - tempList[0])