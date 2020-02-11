#include <stdio.h>
#include <stdlib.h>
#define INF 30000

int** MakeGraph(int N) {
	int** graph = (int**)malloc(sizeof(int*) * N);
	for (int i = 0; i < N; i++)
		graph[i] = (int*)malloc(sizeof(int) * N);

	char* input = (char*)malloc(sizeof(char) * (N+1));
	
	
	for (int i = 0; i < N; i++) {
		scanf("%s", input);
		for (int j = 0; j < N; j++) {
			graph[i][j] = input[j] - '0';
		}
	}

	return graph;
}

struct vertex {
	int r;
	int c;
};

struct De {
	int y;
	int x;
};


int main(void) {
	struct De direct[4];
	int dx[4] = { 0,0,1,-1 };
	int dy[4] = { -1,1,0,0 };
	for (int i = 0; i < 4; i++) {
		direct[i].y = dy[i];
		direct[i].x = dx[i];
	}

	int testCase, N;
	scanf("%d", &testCase);
	for (int t = 1; t <= testCase; t++){
		scanf("%d", &N);
		int** graph = MakeGraph(N);

		int** dist = (int**)malloc(sizeof(int*) * N); //dist 변수 선언. r,c위치에서의 dist값. 초기 값은 INF로 선언해준다.
		for (int i = 0; i < N; i++) {
			dist[i] = (int*)malloc(sizeof(int) * N);
			for (int j = 0; j < N; j++)
				dist[i][j] = INF;
		}
		
		 
		bool** visited = (bool**)malloc(sizeof(bool*) * N); //방문 여부를 확인하는 visited 변수 선언. 초기 값은 false.
		for (int i = 0; i < N; i++) {
			visited[i] = (bool*)malloc(sizeof(bool) * N);
			for (int j = 0; j < N; j++)
				visited[i][j] = false;
		}



		dist[0][0] = 0;
		for (int i = 0; i < N * N; i++) { //N^2 -1 번 반복하여 모든 노드를 방문하자.
			struct vertex minVertex;
			int minCost = INF;			//알고 있는 값 중 최소값을 알려주는 노드 찾기.
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < N; c++) {
					if ((!visited[r][c]) && (dist[r][c] < minCost)) {
						minVertex.r = r;
						minVertex.c = c;
						minCost = dist[r][c];
					};

				}
			}

			
			visited[minVertex.r][minVertex.c] = true;

			struct vertex cur;
			for (int k = 0; k < 4; k++) {
				cur.r = minVertex.r + direct[k].y;
				cur.c = minVertex.c + direct[k].x;
				if (cur.r < 0 || cur.c < 0 || cur.r == N || cur.c == N)
					continue;

				if (dist[cur.r][cur.c] > dist[minVertex.r][minVertex.c] + graph[cur.r][cur.c])
					dist[cur.r][cur.c] = dist[minVertex.r][minVertex.c] + graph[cur.r][cur.c];
			}

		}

		printf("#%d %d\n", t, dist[N - 1][N - 1]);
	}

	return 0;
}
