#include<iostream>
#include<vector>
using namespace std;

void merge(vector<int>& vec, int left, int right, int middle) {
	int leftSize = middle - left + 1;
	int rightSize = right - middle;
	int i = left;
	int mid = (left + right) / 2;
	int j = mid + 1;
	int rock = 2;
	int	scissors = 1;
	int paper = 3;

	while (i <= mid && j <= right) {
		if (vec[i] == -1) {
			i++;
			continue;
		}
		if (vec[j] == -1) {
			j++;
			continue;
		}
		
		if (vec[i] == rock && vec[j] == scissors)
			vec[j] = -1;
		else if (vec[i] == scissors && vec[j] == rock)
			vec[i] = -1;
		else if (vec[i] == rock && vec[j] == paper)
			vec[i] = -1;
		else if (vec[i] == paper && vec[j] == rock)
			vec[j] = -1;
		else if (vec[i] == paper && vec[j] == scissors)
			vec[i] = -1;
		else if (vec[i] == scissors && vec[j] == paper)
			vec[j] = -1;
		else if (vec[i] == vec[j])
			vec[i] = -1;
		
	}
}

void mergeSort(vector<int>& vec, int left, int right) {
	if (left < right) {
		int middle = left + (right - left) / 2;
		mergeSort(vec, left, middle);
		mergeSort(vec, middle + 1, right);

		merge(vec, left, middle, right);
	}
}


int main() {

	int TestCase;
	int	Trial = 1;
	cin >> TestCase;
	while (Trial <= TestCase) {
		int N;
		cin >> N;
		vector<int>vec;
		int elem;
		for (int i = 0; i < N; i++) {
			cin >> elem;
			vec.push_back(elem);
		}
		mergeSort(vec, 0, vec.size() - 1);
		cout << "Trial : ";
		for (int i = 0; i < N; i++) {
			if (vec[i] > 0)
				cout << i << endl;
		}

		++Trial;
	}


	return 0;
}