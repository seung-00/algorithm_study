#include<iostream>
#include<vector>
#include<m>
using namespace std;


int main() {
	int TestCase;
	int Trial = 1;
	cout << "TestCase : ";
	cin >> TestCase;
	while (Trial <= TestCase) {
		cout << endl;
		int max, addTime, index;
		cin >> max >> addTime >> index;
		cout << endl;
		int* arr = new int[max+ addTime];
		int count = 0;
		int a, b, c, d, e;
		/*while (cin >> addVal) {
			*(arr + count) = addVal;d
			++count;
		}*/
		cin >> a >> b >> c >> d >> e;
		cout << endl;
		for (int i = 0; i < 5; i++) {
			if (i == 0)
				arr[i] = a;
			if (i == 1)
				arr[i] = b;
			if (i == 2)
				arr[i] = c;
			if (i == 3)
				arr[i] = d;
			if (i == 4)
				arr[i] = e;
		}
		int newIndex, newVal; //{1,2,3,4,6,5 }
		for (int i = 0; i < addTime; i++) {
			cin >> newIndex >> newVal;
			for (int j = max + (i + 1); j > newIndex; j--) {
				arr[j] = arr[j - 1];
			}
			cout << endl;
			arr[newIndex] = newVal;
		}
		cout << endl;
		cout << "#"<<Trial <<" " <<arr[index];
		Trial++;
	}

	
}