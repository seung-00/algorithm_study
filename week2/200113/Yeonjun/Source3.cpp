#include<iostream>
#include<vector>
#include<ctime>
#include <cstdlib>
#include<algorithm>
using namespace std;

int main() {
	int TestCase;
	int trial;
	cout << "Test case : ";
	cin >> TestCase;
	cout << "\nTrial : ";
	cin >> trial;
	
	while (trial <= TestCase) {
		vector<vector<char>> board(100, vector<char>(100));
		srand(time(NULL));
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				int Random = rand() % 3;
				if (Random == 0)
					board[i].push_back('A');
				else if (Random == 1)
					board[i].push_back('B');
				else if (Random == 2)
					board[i].push_back('C');
			}
		}
		int count = 0;
		int MaxIndex = 99;
		vector<char> Match;
		vector<char> Reverse;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				Reverse.push_back(board[i][MaxIndex - j]);
				for(int k = 0; k< )
				if(Reverse)
			}
		}
	}


	return 0;
}