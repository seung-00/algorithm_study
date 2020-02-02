

# 02 완전탐색 & 그리디
* **재귀함수**  
* **Cominatorial Problems에 대한 완전탐색 방법에 대해 이해**  
* **완전 탐색 문제 해결방법 학습**  
	* baby-gine  
* **탐욕 알고리즘**  
	* 거스름돈 줄이기  
	* Knapsack  
	* 회의실 배정하기  
	* Review baby-gin  
  
## I. 재귀 알고리즘  
* 해결하려는 문제를 **'작은 단위'**로 나누어 동일한 알고리즘을 반복적으로 적용하여 해를 구하는 알고리즘  
* 재귀적 정의는 두 부분으로 나뉨  
1. BASE CASE  
* 집합에 포함되어 있는 원소로 induction을 생성하기 위한 시드(seed)역할.  
	* 여기서 집합이란? merge sort에서 최하위에서 2개의 값만을 비교하여 비교 결과 산출. 이때부터 타고 올라감.  
	따라서 집합이란 최초 문제에서 분할된 문제를 의미하고, 가장 작은 단위가 되어 값을 구할 수 있는 부분. (ex:)merge sort는 값 2개일 때, fact(1) = 1 ...)  
2. 하나 또는 그이상의 유도된 경우(inductive part)  
	* 새로운 집합의 원소를 생성하기 위해 결합되어지는 방법  
	* 따라서 여기서 집합의 의미는 더 작은 문제, 원소는 더 작은 문제에 해당하는 문제의 답들.  
  
  
## II. 조합적 문제  

### 1.순열
####  Traveling Salesman Problem (TSP)  
* 문제 목표 : 모든 도시들을 한 번씩  방문하는데 필요한 최소 비용을 구하라  
* 대다수 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련  
* 서로 다른 것들 중 몇 개를 뽑아서 한 줄 나열  
* n>12인 경우 시간 복잡도 기하급수적 증가  

<**구현**>
  tsp_input.txt
  2
  4
  0 1 2 3
  1 0 4 5
  2 4 0 6
  3 5 6 0
  2th TC...
```{.cpp}  
#include <iostream>
#include <stdio.h>
using namespace std;
#define INF 987654321
#define MAX_N 6
int N, Graph[MAX_N][MAX_N];
int solve(int pos, int visited);
int main()
{   
    int tcCnt;
    freopen("tsp_input.txt", "r", stdin);
    cin >> tcCnt;
    for (int t = 1; t <= tcCnt; ++t) {
        cin >> N;
        for (int i = 0; i <N; ++i)
            for (int j = 0; j<N; ++j)
                cin >> Graph[i][j];

        int ans = INF;
        for (int i = 0; i < N; ++i) {
            int tmp = solve(1, 1 << i);
            if (ans > tmp) ans = tmp;
        }
        cout << "#" << t << ' ' << ans << endl;
    }
    return 0;
}
```


```
int tmp = solve(1, 1 << i);
비트 연산을 통해 visited 표현.
0번 도시 방문시 0번째 bit에 표현.
```

```
int solve(int pos, int visited) //최소 pos = 0 visited = 1
{
    if (visited == (1 << N) - 1) //모든 도시 방문시 방문? -> 10000-1 => 1111
        return 0;

    int ret = INF;
    for (int next = 0; next < N; ++next)
    { // next : 가고자할 목적지
        if (!(visited & (1 << next)) && Graph[pos][next]) //비트에 도시번호 할당했으므로 1<<next
												          //Graph[pos][next] 현위치에서 다음 위치 간선 존재하는지.
												          //이문제는 완전 그래프이므로 항상 존재.
            int tmp = Graph[pos][next] + solve(next,
        {  visited | (1 << next)); // 이 부분을 통해 문제 축소하하였음.
            if (tmp < ret)
                ret = tmp;
        }
    }
    return ret;
}
```

* visited를 array 대신 bit 사용한 이유
	* 메모리 공간 효율적.
	* DP의 memoization 구현시 좋음
		* 4->1>2>3과 1->4->2->3은 2->3 중복계산 발생 
		* int Memo[N][1<<N] 으로 선언. 
			*  [N] 0~N-1 까지의 도시
			*  [1<<N] visited는 0000~1111까지 있음. 그 갯수는 1<<N의 값.
			* 보통 -1을 계산하여 이후 속도 빠르게!

### 2.조합
정의: 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합(combination)이라고 한다.

>$$_nC_r = \frac{n!}{(n-r)!r!}, (n>=r)$$
$$_nC_r = _{n-1}C_{r-1} + _{n-1}C_r$$
$$_nC_0 = 1$$

		
순열 or 조합
* 순열 : 선택의 순서가 결과에 영향
	* {1,2,3,4}에서 2개 골라서 만들 수 있는 최대 수 12 21 34 43..
* 조합 : 선택의 순서가 결과에 영향을 주지 않는 경우
	* 2개를 더해서 만들 수 있는 최대 값

<순열 코드>
```
#include <iostream>
#include <stdio.h>
using namespace std;
// input
// 2
// 4
// 1 2 3 4
// 5
// 2 1 3 5 4

#define MAX_N 10

int N, Nums[MAX_N];
int solve(int cnt, int used, int val);

int main(void) 
{	
	int tcCnt;
	//freopen("numbers_input.txt", "r", stdin);

	cin >> tcCnt;
	for (int t = 1; t <= tcCnt; ++t) {
		cin >> N;
		for (int i = 0; i < N; ++i)
			cin >> Nums[i];
		cout << "#" << t << ' ' << solve(0, 0, 0) << endl;
	}
	return 0;
}

int solve(int cnt, int used, int val) { //cnt 몇개 숫자 선택 used : 어떤 숫자 선택했는지(중복순열아님) val : 
	if (cnt == 2)
		return val;

	int ret = 0; //이 스택에 대해선 ret을 공유하니깐...!! global 선언 안해도 최대값 구할 수 있음.
	for (int i = 0; i < N; ++i) {
		if (used & (1 << i)) continue; //사용 됬는 지 확인.

		int tmp = solve(cnt + 1, used | (1 << i), val * 10 + Nums[i]);  // val*10은 자리 수 올려주는 것. 이진수의 << 연산과 비슷
		if (tmp > ret)
			ret = tmp;
	}
	return ret;
}
```

<조합 코드>
```
#include <iostream>
#include <stdio.h>
using namespace std;

#define MAX_N 10
//input
//2
//4
//1 2 3 4
//5
//2 1 3 5 4
int N, Nums[MAX_N];

int solve(int pos, int cnt, int val);

int main() {
	int tcCnt;

	cin >> tcCnt;

	for (int t = 1; t <= tcCnt; ++t) {
		cin >> N;
		for (int i = 0; i < N; ++i)
			cin >> Nums[i];

		cout << "#" << t << ' ' << solve(0, 0, 0) << endl;
	}
	return 0;
}

int solve(int pos, int cnt, int val) {
	if (cnt == 2) return val;
	if (pos == N) return -1; // 2개 미만 선택했을 경우. 최대값을 고르는 문제이므로 해가 될 수 없는 음의 값 반환.

	int ret = 0, tmp;

	tmp = solve(pos + 1, cnt + 1, val + Nums[pos]); //선택했을 경우
	if (tmp > ret) ret = tmp;

	tmp = solve(pos + 1, cnt, val); //선택 안했을 경우
	if (tmp > ret) ret = tmp; //음수 

	return ret;
}
```
- 부분집합 문제라 생각하고 풀어도 됨.

<조합 코드 - Bit 부분 집합ver.>
```
#include <iostream>
#include <stdio.h>
using namespace std;

#define MAX_N 10
//input
//2
//4
//1 2 3 4
//5
//2 1 3 5 4
int N, Nums[MAX_N];

int solve(); //input을 gloval value로 들고 있기 때문에 input val 필요없음.

int main() {
	int tcCnt;

	cin >> tcCnt;
	for (int t = 1; t <= tcCnt; ++t) {
		cin >> N;
		for (int i = 0; i < N; ++i)
			cin >> Nums[i];

		cout << "#" << t << ' ' << solve() << endl;
	}
	return 0;
}


int countBits(int value) {
	int count = 0;
	while (value > 0) {
		if ((value & 1) == 1)
			count++;
		value = value >> 1;
	}
	return count;
}

int solve() {
	int ret = 0;
	for (int i = 0; i < (1 << N); ++i) { //N개의 원소를 갖는 부분 집합의 수. 1<<N 즉, 가질 수 있는 부분 집합의 수 만큼 반복.
		if (countBits(i) == 2) {
			int sum = 0;
			for (int j = 0; j < N; ++j) {
				if (i & (1 << j))
					sum += Nums[j];
			}
			if (sum > ret) ret = sum;
		}
	}

	return ret;
}
```

## III. 완전탐색
**Baby-gin Game**
* 설명
	* 0~9사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
	*  그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
	* 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.
* 입력 예
	1. 667767은 두 개의 triplet이므로 baby-gin (666,777)
	2. 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin(456,000)
	3. 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 baby-gin이 아니다. (123을 run으로 사용하더라도 011이 run이나 triplet이 아님)
*  어떻게 Baby-gin 여부 판단?
	*  정렬
		*  예제 1,2에 적합하나 234345인 경우 233/445 판단 쉽지 않음(greedy) - **순서가 영향을 준다**
	* Brute-force 이용.

**Brute-force**
* brute-force는 문제를 해결하기 위한 간단하고 쉬운 접근법.
	*  "Just-do-it!"
	*  force의 의미는 컴퓨터의 force 의미.
*  sequential search
	*  자료들의 리스트에서 키 값을 찾기 위해 첫번째 자료부터 비교하며 진행
	* 결과
		*  탐색 성공
		*  탐색 실패
```
int sequentialSearch(int arr[], int n, int x)
{
	for (int i = 0; i < n; i ++) {
		if (arr[i] == x)
			return i;
	}
	return -1;
}
```
* 수행 속도는 느리나 해답 찾을 확률 높음
* 이를 기반으로 백트래킹이나 동적 계획법 통해 알고리즘 개선 가능.
* 많은 종류의 문제들이 특정 조건을 만족하는 경우나 요소를 찾는 것.
* 또한, 이들은 전형적으로 permutation,combination,subsets과 같은 Combinatorial Problems과 연관.
* 완전 탐색은 조합적 문제에 대한 brute-force임.
**완전 탐색을 통한 Baby-gin 접근**
* 고려할 수 있는 모든 경우의 수 생성하기
	* 6개의 숫자로 만들 수 있는 모든 숫자 나열 (중복 포함)
	* ex) {2,3,5,7,7,7} -> 235777, 237577,...... 777532
*  해답 테스트 하기
	*  앞의 3자리와 뒤의 3자리를 잘라, run과 triplet 여부를 테스트하고 최종적으로 baby-gin판단

**Baby-gin Implement Code**
```
#include <iostream>
#include <stdio.h>
using namespace std;

//input
//4
//1 2 4 7 8 3
//6 6 7 7 6 7
//0 5 4 0 6 0
//1 0 1 1 2 3
int Nums[6];
int solve(int arr[], int pos, int used); //pos : 몇번째 숫자 선택 used : 어떤 숫자 사용?

int main() {
	int tcCnt;

	cin >> tcCnt;
	for (int t = 1; t <= tcCnt; ++t) 
	{
		for (int i = 0; i < 6; ++i)
			cin >> Nums[i];

		int arr[6]; //결과를 공통적으로 사용하기 위한 임시 변수  solve에서 pointer가 넘어가기 때문에.
		cout << "#" << t << ' ' << solve(arr,0,0) << endl;  
	}
	return 0;
}

int solve(int arr[], int pos, int used) {
	if (pos == 6) {
		int tri = 0, run = 0;
		for (int i = 0; i < 2; ++i) 
		{
			if (arr[i * 3 + 1] == arr[i * 3]+1 && arr[i * 3 + 2] == arr[i * 3 + 1]+1) // i = 0(앞 3개), arr[1] == arr[0]+1 and arr[2] == arr[1] + 1(차이 1)
				++run;
			else if (arr[i * 3 + 1] == arr[i * 3] && arr[i * 3 + 2] == arr[i * 3 + 1])
				++tri;

		}

		if (run + tri == 2)
			return 1;
		return 0;
	}

	for (int i = 0; i < 6; ++i)
	{
		if (used & (1 << i)) continue;

		arr[pos] = Nums[i];
		if (solve(arr, pos + 1, used | (1 << i)))
			return 1; //결과 값이 1이 나왔다면 1을 propagation(전파,보급,확산)해주는 역할 for 탐색 중도 baby-gin찾으면 종료가능.
	}
	return 0;
}
```

## IV. 탐욕 알고리즘

**문제 제시 : 거스름돈 줄이기**
* 손님이 지불한 금액에서 물건 값을 제한 차액[거스름돈]을 지불하는 문제 생각.
* 어떻게 하면 손님에게 거스름돈으로 주는 지폐와 동전의 개수를 최소한으로 줄일까?

**탐욕[Greedy] 알고리즘이란?**
* 최적해를 구하는데 사용되는 근시안적인 방법
* 여러 경우 중 하나를 선택할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 최종해 도달.
* 각 선택 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 해서 **그것이 최적이란 보장 없음**.

**탐욕 문제 예시**
1.  **800원 거스름돈 걸러줄 때 동전갯수 최소화**
	*  {500,100,50,10}, 500원 1개, 100원 3개  =>최적해.
	*  {500,400,100,50,10}, 400원 2개가 최적해. 즉, 500원 1개, 100원 3개는 최적해가 아님.

2. **배낭 짐싸기[Knapsack]**
배낭에 담을 수 있는 총무게 정해져 있고,<br>각 물건의 무게와 가치가 있음, 이때 최대 가치값은?

||무게|값|
|------|---|---|
|물건1|25kg|10만원|
|물건2|10kg|9만원|
|물건3|10kg|5만원|

* **[접근1]Knapsack에 대한 완전 탐색 기법**
	* 완전 탐색으로 물건들의 집합 S에 대한 모든 부분집합을 구한다.
	* 부분집합의 총무게가 W를 초과하는 집합들은 버리고, 나머지 집합에서 총 값이 가장 큰 집합을 선택할 수 있다.
	* 물건의 개수가 증가하면 시간 복잡도가 지수적 증가.
* **[접근2]Knapsack에 대한 탐욕적 방법1**
	*  값이 비싼 물건부터 채운다
	*  W  = 30kg
	* 탐욕적 방법의 결과
		* 물건1,25kg,10만원
	* 최적해
		*  (물건2, 물건3), 20kg, 14만원
	* 최적이 아님.


* **[접근3]Knapsack에 대한 탐욕적 방법2**

||무게|값|
|------|---|---|
|물건1|25kg|10만원|
|물건2|10kg|9만원|
|물건3|10kg|5만원|

*
	* 무게가 가벼운 물건부터 채운다.(왠지 많이 채우니까 가치높을 것 같아)
	* W = 30kg
	* 탐욕적 방법
		* (물건1,물건3)  14만원
	*  최적해
		* (물건1) 15만원
	*  최적해 구할 수 없음.

* **[접근4]Knapsack에 대한 탐욕적 방법3**

||무게|값|값/kg|
|------|---|---|---|
|물건1|5kg|50만원|10만원/kg|
|물건2|10kg|60만원|6만원/kg|
|물건3|20kg|140만원|7만원/kg|
 * 무게 당 (예 >kg당) 값이 높은 순서로 물건을 채운다.
* 역시 최적해 못구함

3. **Fractional Knapsack 문제**
	* 물건 잘라 넣을 수 있음.
	* 탐욕적 방법으로 최적해 가능
4. **회의실 배정하기**(활동선택문제)
	* 문제 설명
		* 김대리는 소프트웨어 개발팀들의 회의실 사용 신청을 처리하는 업무를 한다. 이번 주 금요일에 사용 가능한 회의실은 하나만 존재하고 다수의 회의가 신청된 상태이다. (문제 편의를 위해 요일 고정)
		* 회의는 시작 시간과 종료 시간이 있으며, 회의 시간이 겹치는 회의들은 동시에 열릴 수 없다.
		* 최대 몇 개의 회의를 배정할 수 있을까?
		* 입력 예
			* 회의 개수
			* (시작시간, 종료시간)
	* 탐욕기법 적용 .
		1. 회의 목록 S에서 가장 일찍 끝나는 회의 a_min을 선택한다.
		2. a_min과 곂치는 모든 회의를 S에서 삭제한다.
		3. S에 회의가 모두 없어질 때까지, 1번부터 반복
	* 정당성 증명
		* 탐욕적 선택이 항상 최적해로 가는 길 중에 하나이다.
		* 즉, 가장 종료 시간이 빠른 회의를 포함하는 최적해가 반드시 존재한다.
![텍스트](https://postfiles.pstatic.net/MjAyMDAyMDNfMTA1/MDAxNTgwNjYzNTQxODcx.LWhKIWL6FrMKgxZrDtARwvWQcebM901tP-UVn2veZ8og.ywl1gxKUNEDdIkJjxwyzn4Yz4Tla8921qqxXJWxLlbEg.PNG.solution_12/%EC%BA%A1%EC%B2%98.PNG?type=w773)

**MeetingRoom implement code**
```
#include <iostream>
#include <stdio.h>
using namespace std;

//input
//10
//1 4 1 6 6 10 5 7 3 8 5 9 3 5 8 11 2 13 12 14

struct meeting_type { 
	int start;
	int end;
};

int N;
meeting_type Meetings[10];

int solve();

int main() {

	cin >> N;
	for (int i = 0; i < N; ++i)
		cin >> Meetings[i].start >> Meetings[i].end;

	cout << solve() << endl;

	return 0;
}

int solve() {
	for (int i = 0; i < N - 1; ++i) { //sorting 단순화.
		for (int j = i + 1; j < N; ++j) {
			if (Meetings[i].end > Meetings[j].end) {
				meeting_type tmp = Meetings[i];
				Meetings[i] = Meetings[j];
				Meetings[j] = tmp;
			}
		}
	}

	int lastEnd = 0, cnt = 0;
	for (int i = 0; i < N; ++i) {
		if (Meetings[i].start < lastEnd) continue;

		printf("(%d,%d)\n", Meetings[i].start, Meetings[i].end);
		lastEnd = Meetings[i].end;
		++cnt;
	}
	return cnt;
}
```

5. Baby-gine - 탐욕 기법 접근
	* 탐욕기법으로 풀어보는 이유. (문제풀이 시도를 위해)
	* 접근 방법
		* 0~9번호별 카드의 개수를 counts 배열에 센다
		* counts 배열의 각 원소를 체크하여 run과 triplet를 확인하여 baby-gin여부를 판단.
	* ![](https://postfiles.pstatic.net/MjAyMDAyMDNfMTU5/MDAxNTgwNjY1NDk5MDUx.HgZwvsLnbDcoA-gVzhir4S-WA30wp2D8PuN3H_AuSEcg.7Fkd0aVBuL5zBQi7xAQV_ZFzGtfUiw2CAVAigkPpcvwg.PNG.solution_12/%EC%BA%A1%EC%B2%982.PNG?type=w773)
	* run과 triplet 어떤 것을 먼저 파악?
		* 333456에서 run먼저 판단한다면 345 -> run error! =>triplet먼저 판단 해야한다.
		*  **항상 예외 케이스를 파악하여 조건 순서에 맞게 작성**

**Baby-gin Greedy ver. Implement Code**
```
#include <iostream>
#include <stdio.h>
using namespace std;

//input
//4
//1 2 4 7 8 3
//6 6 7 7 6 7
//0 5 4 0 6 0
//1 0 1 1 2 3
int Nums[6], Cnt[10];
int solve(); //pos : 몇번째 숫자 선택 used : 어떤 숫자 사용?

int main() {
	int tcCnt;

	cin >> tcCnt;
	for (int t = 1; t <= tcCnt; ++t) 
	{
		for (int i = 0; i < 10; ++i)
			Cnt[i] = 0;

		for (int i = 0; i < 6; i++) {
			cin >> Nums[i];
			Cnt[Nums[i]]++;
		}

		cout << "#" << t << ' ' << solve() << endl;  
	}
	return 0;
}

int solve()
{
	int tri = 0, run = 0;
	for (int i = 0; i < 10; ) {
		if (Cnt[i] >= 3) {
			Cnt[i] -= 3;
			tri++;
		}
		else if (i <= 7 && Cnt[i] >= 1 && Cnt[i + 1] >= 1 && Cnt[i + 2] >= 1) {
			Cnt[i]--;
			Cnt[i + 1]--;
			Cnt[i + 2]--;
			run++;
		}
		else {
			++i;
		}
	}

	if (tri + run == 2)
		return 1;

	return 0;
}

```
