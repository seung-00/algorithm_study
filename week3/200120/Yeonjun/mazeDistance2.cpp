//#include <iostream>
//#include <string>
//#include <queue>
//#include <set>
//#include <cmath>
//using namespace std;
//
//int path_finder(string maze)
//
//{
//	// TODO: Return the minimal number of steps required to reach the exit located at
//	// (n - 1, n - 1) from the initial position (0, 0) in an n × n maze if possible an
//	// -1 otherwise
//
//	int N = sqrt(maze.size()); //N*N 미로의 N
//
//	if (N == 1) //(0, 0)만 있다면 0번 걷는다
//		return 0;
//
//	set<int> visited; //방문한 곳 표시
//	visited.insert(0); //0, 0 방문
//
//	queue<pair<int, int>> curStatus; //현재 상황
//
//	curStatus.push(pair<int, int>(0, 0));
//
//
//
//	while (!curStatus.empty())
//
//	{
//		pair<int, int> current = curStatus.front();
//
//		//현 위치 정보 + 누적 걸음수
//
//		int place = current.first;
//		int steps = current.second;
//		curStatus.pop();
//
//		int up = place - N - 1; //북
//		int down = place + N + 1; //남
//		int left = place - 1; //서
//		int right = place + 1; //동
//
//		//다음 위치
//		int nextIdx[] = { up, down, left, right };
//
//		for (int i = 0; i < 4; i++)
//		{
//			if (nextIdx[i] < 0) //범위를 벗어난다면
//				continue;
//
//			if (nextIdx[i] >= maze.size()) //마찬가지로 범위를 벗어난다면
//				continue;
//
//			if (visited.count(nextIdx[i])) //이미 방문했다면
//				continue;
//
//			if (maze[nextIdx[i]] != '.') //방문할 수 있는 곳이 아니라면
//				continue;
//
//			visited.insert(nextIdx[i]); //방문했다고 표시
//			curStatus.push(pair<int, int>(nextIdx[i], steps + 1)); //현재 위치, 누적 걸음수
//
//			if (nextIdx[i] == maze.size() - 1) //목적지에 도달할시
//				return steps + 1;
//		}
//	}
//	return -1;
//}
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//int main(void)
//
//{
//
//	cout << path_finder(".W.\n.W.\n...") << endl;
//
//	cout << path_finder(".W.\n.W.\nW..") << endl;
//
//	cout << path_finder("......\n......\n......\n......\n......\n......") << endl;
//
//	cout << path_finder("......\n......\n......\n......\n.....W\n....W.") << endl;
//
//	return 0;
//
//}
//
