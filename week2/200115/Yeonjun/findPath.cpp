#include<iostream>
#include<vector>
#include<string>
#include<vector>
using namespace std;

void dfs(int start, int end, vector<vector<int>>& vec, vector<bool>& visited, bool& Found, int i) {
	cout << "\nVisiting " << start << endl;
	visited[i] = true;
	int length = vec[start].size();
	for (int j = 0; j < length; j++) {
		int newStart = vec[start][j];
		if (newStart == end) {
			Found = true;
			return;
		}
		else {
			if(!visited[newStart])
				dfs(newStart, end, vec, visited, Found, i);
		}
	}
}

void findWay(int start, int end, vector<vector<int>>& vec, vector<bool>& visited, bool& Found) {
	int length = vec[start].size();
	for (int i = 0; i < length; i++) {
		if (Found == true)
			return;
		if(!visited[i])
			dfs(start, end, vec, visited, Found, i);
	}
}

// Driver code 
int main() {
	int TestCase;
	int Trial = 1;
	cout << "TestCase : ";
	cin >> TestCase;
	while (Trial <= TestCase) {
		int V, E;
		cout << "\nVertex and Edge : ";
		cin >> V >> E;
		vector<vector<int>>adj(V+1);
		vector<bool>visited(V+1,0);
		for (int i= 0; i < E; i++) {
			int from, to;
			cin >> from;
			cin >> to;
			adj[from].push_back(to);
		}
		int start, end;
		cin >> start >> end;
		bool found = false;
		findWay(start, end, adj, visited, found);
		cout << endl << "#" << Trial << " " << found;
		++Trial;
	}

	return 0;
}
