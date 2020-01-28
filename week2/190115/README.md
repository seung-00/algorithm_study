# 190115

## 스택

* top: 마지막에 삽입된 원소의 위치

* ADT

  * push: 삽입, pop: 삭제, isEmpty: 비었는지 peek: top 원소 반환

* 파이썬에서 리스트로 스택 구현  

* 스택 응용 예시: 괄호 검사

  <img src="https://user-images.githubusercontent.com/46865281/72344197-fd316300-3713-11ea-9cdd-68d3512786a9.png" alt="image" style="zoom:20%;" />



## 재귀

* 재귀 함수를 쓸 경우, 함수를 스택에 쌓으며 함수 호출을 하므로 메모리의 사용량이 증가한다는 문제점이 생긴다.
* 반복 함수에서는 하나의 변수에서 계산된 값만 유지하면 되는데 재귀함수면 입력 값, 결과 값을 모두 복사하는 식의 오버헤드 발생
* 그럼에도 직관적으로 코드를 짤 수 있는 경우가 존재하므로 쓰임



## 메모이제이션

* 한 번 계산한 결과를 메모리에 저장해두고 꺼내 씀으로써 중복 계산을 피하는 방법이다. DP에 쓰임

* 중복 계산 예시: 피보나치 수열

  <img src="/Users/seungyoungoh/Library/Application Support/typora-user-images/image-20200114214639737.png" alt="image-20200114214639737" style="zoom:30%;" />

  예컨대 f(4) = f(1)+f(0)+f(1)+f(1)+f(0)으로 같은 값이 계속 중복된다.

* 메모이제이션을 적용한 피보나치 수열

  ```python
  def fibo(n):
    global memo
    if n>=2 and len(memo)<=n:
      memo.append(fibo(n-1) + fibo(n-2))
     return memo[n]
  	memo = [0, 1]
  ```

  

## 동적 계획법(DP)

* 크기가 작은 문제들은 모두 해결하고 그 해들을 이용해 보다 큰 크기의 문제들을 해결

  * 문제를 부분들로 나누고, 부분들의 해를 테이블에 저장한 후 이를 이용한다.

* 피보나치 수에 DP 적용

  ```python
  def fibo(n):
    f = [0, 1]
    for i in range(2, n+1):
      a.append(f[i-1]+f[i-2])
    return fibo[n]
  ```



## 깊이 우선 탐색(DFS)

![image](https://user-images.githubusercontent.com/46865281/72500441-d0965c00-3877-11ea-94be-d61c7db3f8db.png)

* 코드

  ```python
  def DFS(graph, root):
      visited = []
      stack = []
      stack.append(root)
  
      while stack:
          node = stack.pop()
          visited.append(node)
          childNode = list((graph[node]) - set(visited))   #자식 노드 중 아직 안 간 곳
          stack.extend(childNode)
  #graph = {1:{4, 3}, 2:{3, 5}, 3:{}, 4:{6}, 5:{}, 6:{}}
  ```

  

* 재귀로 구현

  ```python
  def DFS(graph, node, visited = []):
      if node not in visited:
          print(node)
          visited.append(node)
      for neighbour in graph[node]:
          DFS(graph, neighbour, visited)
  ```

  다른 코드

  ```python
  def DFS(graph, node, visited = []):
      visited.append(node)
      print(node)
      childNode = list((graph[node]) - set(visited))   #자식 노드 중 아직 안 간 곳
      while childNode:
          DFS(graph, childNode.pop(), visited)
  ```
  * 딕셔너리가 경로 저장하기 좋다, set을 쓰면 방문한 노드를 제외하기 좋다.

  * 트리 구조를 재귀로 만들 때 주의할 점은 분기가 나눠진다는 점이다. for 이나 while로 분기를 나눠줘야 한다. **재귀는 그저 스택의 역할을 대신 수행할 뿐이다.** 일반적인 재귀문처럼 return으로 값을 반환하려고 하면 반복문이 끝나고 나눠진 분기들을 순회할 수 없다.

     

    