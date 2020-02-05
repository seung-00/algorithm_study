# 200224

## 분할 정복

* 예제

  >n 개의 동전들 중 가짜 동전이 하나 포함되어있다. 가짜 동전은 진짜 동전에 비해 아주 조금 가볍다. 진짜 동전들의 무게가 동일하다고 할 때 양팔 저울을 이용해서 가짜 동전을 찾자.
  >
  >양팔 저울을 최소로 사용해서 가짜 동전을 찾는 방법은?
  >
  >예컨대 동전이 24(진짜 23, 가짜 1)개 있다면?
  >
  >12, 12 비교 => 6, 6 비교 => .... 분할 정복

  

* 예제 2. 거듭제곱

  * 일반적인 재귀로 풀 경우 O(n)의 시간 복잡도

    ```c++
    int GetPower(int x, int n)
    {
    	if (n == 0) return 1;
    	if (n == 1)	return x;
    	
    	return x * GetPower(x, n-1);
    }
    ```

    

  * 분할 정복 기법 사용, O(log n)

    ```c++
    int DCPower(int x, int n)
    {
    	if (n == 0)	return 1;
    	if (n == 1)	return x;
    	
    	if (n % 2 == 0)
    	{
    		int ret = DCPower(x, (n/2);
    		return ret * ret;
    	}
    	else
    	{
    		int ret = DCPower(x, (n-1)/2);
    		return ret * ret * x; 
    	}
    }
    ```

  

## 병합 정렬

1. 분할 단계: 최소 크기의 부분집합이 될 때까지 분할 반복

2. 병합 단계: 2개의 부분집합을 정렬하면서 하나의 집합으로 병합 

   ```c++
   void MergeSort(int arr[], int size)
   {
     if (size == 1) return;
     
   	// 분할
     int mid = size /2;
     MergeSort(arr, mid);
     MergeSort(arr + mid, size - mid);
     // 배열 주소를 mid 만큼 옮겨서 전달함
   
     // 임시 버퍼
     int * buf = new int[size];
     int i = 0, j = mid, k =0;
     // i 는 왼쪽 배열, j는 오른쪽 배열 각각 비교해서 병합을 위한 배열에 넣어줌 
     while (i < mid && j < size)
       buf[k++] = arr[i] < arr[j] ? arr[i++] : arr[j++];
     
   	// 왼쪽 혹은 오른쪽이 남음
     while (i < mid)	
       buf[k++] = arr[i++];
   
     while (i < size)
       buf[k++] = arr[j++];
   
   	// 정렬된 값으로 덮어 써줌  
     for (i = 0; i<size; ++i)
       arr[i] = buf[i]
       
     delete buf;
   }
   ```



* **시간 복잡도: O(n log n)**

  <img src="https://user-images.githubusercontent.com/46865281/73808275-aef31980-4812-11ea-8bd1-6b7d686c470f.png" alt="image" style="zoom:33%;" />



## 퀵 정렬

* 주어진 배열을 두 개로 분할하고 각각을 정렬한다.

* 병합정렬과 다른 점

  1. 병합정렬은 그냥 두 부분으로 나누는 반면, 퀵 정렬은 분할할 때 피벗을 중심으로 이보다 작은 것을 왼편, 큰 것을  오른편에 위치 시킴
  2. 병합정렬은 각 부분 정렬이 끝난 후 "병합" 작업이 필요하나 퀵정렬은 필요 없음

*  Idea: 피벗보다 작은 걸 왼쪽, 큰 걸 오른쪽에 둠으로써 **피벗의 위치**를 찾아준다.

* 과정

  1. 피벗은 보통 왼쪽 끝 값으로 지정한다.

     왼쪽에서 피벗보다 큰 값이 나올 때까지 이동 하고 오른쪽에서 피벗보다 작은 값이 나올 때까지 이동한다. 둘 다 나올시 이동을 멈추고 둘을 바꿔줌으로써 작은 값, 큰 값 분류를 한다. 

  <img src="https://user-images.githubusercontent.com/46865281/73808078-fdec7f00-4811-11ea-894e-d618018f4547.png" alt="image" style="zoom:46%;" />

  <img src="https://user-images.githubusercontent.com/46865281/73808060-ead9af00-4811-11ea-8832-53fc4aa94644.png" alt="image" style="zoom:40%;" />

  

  2. 두 값이 교차했다면, 그 지점은 피벗의 위치다(비록 완벽히 정렬이 안 됐어도 작은 값, 큰 값의 개수가 자리를 차지하고 있기 때문) 피벗과 j(교차된 값, 피벗보다 작은 값)를 바꿔서 피벗의 위치를 정해준다.

  <img src="https://user-images.githubusercontent.com/46865281/73808048-df868380-4811-11ea-9503-3cebc050e706.png" alt="image" style="zoom:33%;" />

  

   3.  피벗 기준의 두 파트들도 같은 연산을 재귀적으로 반복해준다.

       <img src="https://user-images.githubusercontent.com/46865281/73808035-d695b200-4811-11ea-9e6c-2ea14fed513d.png" alt="image" style="zoom:33%;" />

       <img src="https://user-images.githubusercontent.com/46865281/73808022-c8479600-4811-11ea-822b-84e3cbc42d5b.png" alt="image" style="zoom:35%;" />

```c++
#include <iostream>
using namespace std;

void QuickSort(int arr[], int left, int right)
{
    if (left < right)    // 이 둘이 같으면 사이즈가 1이라는 뜻
  {
    int p = left, i = left + 1, j = right;
    while (i<=j)    // 교차하면 거기가 피벗 위치
    {
      while (arr[i] <= arr[p]) i++;
      while (arr[j] > arr[p]) j--;
      
      if (i<j)    // 아직 교차 x
      {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
      }
    }
    int tmp = arr[p];
    arr[p] = arr[j];
    arr[j] = tmp;
    
    QuickSort(arr, left, j-1);
    QuickSort(arr, j+1, right);
  }
}

int main()
{
    int arr[] = {20, 2, 1, 1, 0};
    QuickSort(arr, 0, 4);
    
    for(int i = 0; i<5; i++)
    {
        cout<<arr[i];
    }
    cout<<endl;
}

```

* **시간 복잡도: O(nlog n)** (병합 정렬과 마찬가지)



## 이진탐색

```c++
int BinarySearch(int arr[], int low, int high , int key)
{
  #base case 1
  if (low > high) return -1;
  
  int mid = (low+high)/2;
  #base case2
  if (arr[mid] == key)	return mid;
  
  else if (arr[mid] > key)	return BinarySearch(arr, low, mid-1, key);
  
  else	return BinarySearch(arr, mid+1, high, key);
}
```

* **시간 복잡도: O(log n)**

  <img src="https://user-images.githubusercontent.com/46865281/73808000-b665f300-4811-11ea-9a06-313efa035252.png" alt="image" style="zoom:55%;" />

  



## 백트래킹

* 백트래킹

  * 상태 공간 트리를 깊이 우선 탐색할 때, 각 상태 노드에서 해가 될 가능성이 없는 자식 노드의 탐색을 진행하지 않는다. (**Prunning**, 가지치기)

* 예시: N-Queen

  > n x n 체스판에 배치한 퀸들이 서로 위협하지 않도록 n 개의 퀸을 배치하라.
  >
  > 어떤 두 퀸도 서로를 위협하지 않도록, 퀸을 배치한  n 개의 위치는?
  * 8-퀸이라 하자. 8x8의 64개 판 중 8개의 위치를 정한다.

    조합으로 생각하면 매우 많은 경우의 수(64_C_8)

    실제 해는 92개 뿐이므로 완전 탐색하면 너무 많은 시간이 걸림

  * 4-퀸이라 축소해서 생각해보자. 

    * **같은 행에 위치할 수 없다** 라는 조건을 생각하며 트리를 짜면 다음과 같이 경우의 수가 줄어든다(4x4x4x4 = 256).

      <img src="https://user-images.githubusercontent.com/46865281/73807976-9cc4ab80-4811-11ea-90b7-da49ab162b5b.png" alt="image" style="zoom:50%;" />

      

    * **백트래킹** 적용, 자식의 유망성을 점검한 후에 유망하지 않다고 결정되면 부모로 돌아가서 다음 자식 노드로 감

      이 경우, 지금까지 놓은 퀸이 다른 퀸을 위협하지 않는 경우 유망하다고 생각할 수 있음 

      <img src="https://user-images.githubusercontent.com/46865281/73809066-53765b00-4815-11ea-93bf-e805167ae305.png" alt="image" style="zoom:44%;" />

      <img src="https://user-images.githubusercontent.com/46865281/73809158-b0721100-4815-11ea-935e-568a1036a472.png" alt="image" style="zoom:38%;" />

      

      ```c++
      #include <stdio.h>
      #define ABS(x)	(x > 0 ? x : -(x))
      int N, Row[100] = {0};
      // 거리 구하기 쉽게 ABS 정의해줌
      // 행들만 비교할 거니까 Row 1차원으로 2차원 표현했음. 행이 인덱스, 열이 값
      
      void PrintResult()
      {
        static int cnt = 1;
        printf("%3d Result : ", cnt++);
        for (int i = 1; i<=N; ++i)	printf("(%d, %d)", i, Row[i]);
        // i: 행, Row[i]: 열
        printf("\n");
      }
      
      // 새로운 퀸 q 와 앞선 퀸들을 비교한다.
      bool Primising(int q)
      {
        for (int i = 1; i<q; ++i)
        {
          // 1. 열을 비교
          // 2. 대각선으로 위협이 되는가? => dx == dy 여부
          if (Row[q] == Row[i] || ABS(Row[q] - Row[i]) == ABS(q-i))	return false; 
        }
        
        return true;
      }
      
      
      void Queens(int q)
      {
        // base case
        if (!Primising(q)) return;	// 이 부분이 가지치기. 이 코드 없으면 순수 완전 탐색
        
        // 만약 가지치기가 없으면 아래 코드가 256번 실행될 것임
        if (q == N)
        {
          PrintResult();
          return;
        }
        
        for (int i =1; i<= N; ++i)
        {
          // 기본적으로 완전 탐색
          // 1행부터 시작, 각 행마다 재귀호출
          Row[q+1] = i;
          Queens(q+1);
        }
      }
      
      int main()
      {
        scanf("%d", &N);
        Queens(0);
        return 0;
      }
      
      ```

      

