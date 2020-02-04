//#include<iostream>
//#include<string>
//#include<cmath>
//using namespace std;
//
//
//int main() {
//
//	int TestCase;
//	cout << "Case :";
//	cin >> TestCase;
//	int trial = 1;
//	while (trial <= TestCase) {
//		string str1, str2;
//		cout << "\nstring N: ";
//		cin >> str1;
//		cout << "\nsting M: ";
//		cin >> str2;
//
//		if (str1.length() < 5 || str1.length() > 50 || str2.length() < 10 || str2.length() > 1000) {
//			cout << "error..";
//		}
//
//		else if (str1.find(str2) >= 0) {
//			cout <<"\n#"<< trial <<": 1";
//		}
//		else {
//			cout << "\n" << trial << ": 0";
//		}
//		cout << endl;
//		++trial;
//	}
//
//	return 0;
//}