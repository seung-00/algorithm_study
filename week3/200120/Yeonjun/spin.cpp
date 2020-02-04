//#include<iostream>
//#include<vector>
//#include<queue>
//using namespace std;
//
//int main() {
//
//	int TestCase;
//	int	Trial = 1;
//	cin >> TestCase;
//	while (Trial <= TestCase) {
//		int N, M;
//		cin >> N >> M;
//		//queue std for Queue
//		queue<int> Que;
//		int element;
//		//Push element N times
//		for(int i =0; i< N; ++i) {
//			cin >> element;
//			Que.push(element);
//		}
//		//Do putting front element to rear part M times
//		for (int i = 0; i < M; i++) {
//			int front = Que.front();
//			Que.pop();
//			Que.push(front);
//		}
//		cout <<"#" << Trial << " " <<Que.front() << endl;
//		Trial++;
//	}
//
//	return 0;
//}