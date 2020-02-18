//#include<iostream>
//#include<vector>
//using namespace std;
//
//int getMin(vector<vector<int>>& vec, int N) {
//	
//	int total = 0;
//	for (int i = 0; i < N; i++) {
//		vector<int> current(N);
//		int minimum = 0;
//		for (int j = 0; j < N; j++) {
//			for (int k = 0; k < current.size(); k++) {
//				if (j == current[k])
//					++j;
//			}
//			if (j == 0)
//				minimum = vec[i][j];
//			else {
//				if (minimum > vec[i][j]) {
//					minimum = vec[i][j];
//					current.push_back(minimum);
//				}
//			}
//		}
//		int temp = 0;
//		for (int p = 0; p < N; ++p) {
//			temp += current[p];
//		}
//		if (temp < total)
//			total = temp;
//	}
//	return total;
//	
//}
//
//
//int main() {
//	
//	int TestCase, Trial;
//	Trial = 0;
//	cout << "Test case : ";
//	cin >> TestCase;
//	while (Trial < TestCase) {
//		int N;
//		cout << "\nN : ";
//		cin >> N;
//		vector<vector<int>> square(N, vector<int>(N));
//		int size = N * N;
//		for (int i = 0; i < size; i++) {
//			for (int j = 0; j < N; j++) {
//				int num;
//				cin >> num;
//				square[i][j] = num;
//			}
//		}
//		cout << endl;
//		cout << getMin(square, N) << endl;
//		Trial++;
//	}
//
//
//	return 0;
//}