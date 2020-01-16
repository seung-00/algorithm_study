# 20190113

## 문자열

### C 의 경우

* 가변 길이, 딜리미터 기준으로 길이 조절

* 문자열 끝에 '\0', char arr[] = {'a', 'b', 'c', '\0'}
* strlen(), strcpy(), strcmp() 등 문자열 처리 함수



### JAVA의 경우

* 가변 길이, 길이 조절 가능(string 클래스 내에 스트링 길이가 존재함)

* string str = "abc"
* +, length(), replace(), split() 등 문자열 처리 메소드 



### Python의 경우

* 문자열은 튜플과 같이 **불변**

* char 타입이 없음, 텍스트 데이터 취급 통일
* replace(), split() 등의 문자열 처리 메소드
* 불변이므로 값이 변경되는 메소드를 써도 원본 데이터가 아닌 새로운 데이터를 만들어서 리턴하는 것





## 패턴 매칭

### 고지식한 알고리즘(Brute Force)

* 문자열 처음부터 끝까지 순회하며 비교

* 최악의 경우 시간 복잡도: O(MN)

  ```python
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
    if j == M: return i - M # 검색 성공
    else: return -1	#검색 실패
  ```



### KMP 알고리즘

* 최악: O(MN),  최선: O(N)

* 파이썬으로 구현해보기



### 보이어-무어 알고리즘 

* 최악: O(MN), 최선: O(N)보다 적음
* 오른쪽에서 왼쪽으로 비교, 상용 소프트웨어에서 쓰임

<img src="https://user-images.githubusercontent.com/46865281/72220608-9dad4900-3595-11ea-9ad2-762afbb6bd3a.png" alt="image" style="zoom:30%;" />



```python
def Boyer_Moore(pattern, string):
    sLen = len(string)
    pLen = len(pattern)
    badMatchTable = {key: pLen - pattern. index(key) - 1
                    for key in pattern[:-1]}
    i = pLen - 1
    last = pattern[i]
    while i < sLen:
        char = string[i]
        if char == last:
            first = i - pLen + 1
            if string[first:i+1] == pattern:
                return 1
        i += badMatchTable.get(char, pLen)  #char에 일치하는 값이 없을 시 plen만큼 이동
    return 0
```

