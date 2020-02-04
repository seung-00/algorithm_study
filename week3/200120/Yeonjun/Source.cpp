#include<iostream>
using namespace std;

int main() {
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case) {
		int N;
		cin >> N;
		int length = 0;
		char original[20];
		char seokChan[20];
		cin >> original >> seokChan;
		int correct = 0;
		for (int i = 0; i < N; i++) {
			if (original[i] == seokChan[i])
				++correct;
		}
		cout << "\n#" << test_case << " " << correct;
	}

	return 0;
}