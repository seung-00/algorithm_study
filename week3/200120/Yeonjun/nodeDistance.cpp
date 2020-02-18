//#include<iostream>
//#include<vector>
//#include<queue>
//using namespace std;
//
//int bfs(vector<vector<int>>& vertexWays, vector<int>& visited, int start, int end) {
//	int pathCount = 0;
//	queue<pair<int, int>> path;
//	visited[start] = true;
//	path.push(pair<int, int>(start,pathCount));
//	while (!path.empty()) {
//		int newStart = path.front().first;
//		int totalCount = path.front().second;
//		cout << "Newest node : " << newStart << endl;
//		path.pop();
//		int length = vertexWays[newStart].size();
//		for (int i = 0; i < length; i++) {
//
//			int linkedNode = vertexWays[newStart][i];
//			if (visited[linkedNode] == 0) {
//				cout << "Inside " << linkedNode << endl;
//				visited[linkedNode] = true;
//				if (linkedNode == end) {
//					cout << "Found.. "<< endl;
//					return totalCount+1;
//				}
//				path.push(pair<int, int>(linkedNode, totalCount+1));
//			}
//		}
//	}
//	/*if (!visited[start]) {
//		int length = vertexWays[start].size();
//		cout << "never visited " << start << " node..." << endl;
//		visited[start] = true;
//		path.push(start);
//		cout << "pushed " << start << "....." << endl;
//		cout << "current queue size " << path.size() << endl;
//		int filled = 1;
//		bool flag = false;
//		for (int i = 0; i < length; i++) {
//			int connectedNode = vertexWays[start][i];
//			if (connectedNode == end) {
//				cout << "connected" << endl;
//				possibleWays.push_back(path.size());
//			}
//			else if (visited[connectedNode]) {
//				cout <<start <<" to " <<  connectedNode << "is already visited..." << endl;
//				filled++;
//				flag = true;
//			}
//			if (filled == length && flag == true) {
//				if (path.size() != 0) {
//					cout << "adj nodes all filled poping this node from queue" << endl;
//					path.pop();
//				}
//			}
//			if(visited[connectedNode]){
//				cout << connectedNode << "is already visited..." << endl;
//				filled++;
//				
//			}
//		}
//		for (int i = 0; i < length; i++) {
//			int connectedNode = vertexWays[start][i];
//			bfs(vertexWays, visited, connectedNode, end, path, possibleWays);
//		}
//	}
//	else {
//		cout << start << "bfs parameter function is visited... doing nothing and ending function" << endl;
//	}*/
//}
//
//int main() {
//	int TestCase;
//	int Trial = 1;
//	cout << "testCase : ";
//	cin >> TestCase;
//	cout << endl;
//	while (Trial <= TestCase) {
//		int vertex, edge;
//		cin >> vertex >> edge;
//		vector<int>visited(vertex + 1, 0);
//		vector<vector<int>>vertexWays(vertex + 1);
//		vector<int>possibleWays;
//		for (int i = 0; i < edge; i++) {
//			int from, to;
//			cin >> from >> to;
//			vertexWays[from].push_back(to);
//			vertexWays[to].push_back(from);
//		}
//		int start, end;
//		int minWay = 0;
//		cin >> start >> end;
//		minWay = bfs(vertexWays, visited, start, end);
//		if (minWay == 0)
//			cout << "\n#" << Trial << "Path doesn't exist..." << endl;
//		else
//			cout << "\n#" << Trial << " " << minWay << endl;
//		Trial++;
//	}
//
//	return 0;
//}