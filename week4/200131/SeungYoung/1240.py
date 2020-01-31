def CheckPwd(numList):
    if ((numList[0] + numList[2] + numList[4] + numList[6])*3 + numList[1]+numList[3]+numList[5]+numList[7])%10 == 0:
        return True


def CheckNum(num):
    if num == "0001101": return 0 
    elif num == "0011001": return 1
    elif num == "0010011": return 2
    elif num == "0111101": return 3
    elif num == "0100011": return 4
    elif num == "0110001": return 5
    elif num == "0101111": return 6
    elif num == "0111011": return 7
    elif num == "0110111": return 8
    elif num == "0001011": return 9

def GetPwd(target): # target is str
    rst = []
    for pivot in range(len(target)-7):
        temp = target[pivot:pivot+7]
        if temp[0] == '0' and temp[-1] == '1':
            tempNum = CheckNum(temp)
            if tempNum:
                rst.append(tempNum)
                target = target[pivot+7: pivot+56]
                for j in range(7):
                    rst.append(CheckNum(target[j*7:(j+1)*7]))
                break
    return rst



rst = GetPwd("00000000000000011101101100010111011011000101100010001101001001101110110000000000")
print(rst)
print(CheckPwd(rst))
