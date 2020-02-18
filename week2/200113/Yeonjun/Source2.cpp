//#include<iostream>
//#include<string>
//#include<vector>
//using namespace std;
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
//		vector<char> alphabet;
//		for (int i = 0; i < str1.length(); ++i) {
//			if (i == 0)
//				alphabet.push_back(str1[i]);
//			else {
//				for (int j = 0; j < alphabet.size(); j++) {
//					if (str1[i] == alphabet[j])
//						break;
//					alphabet.push_back(str1[i]);
//				}
//			}
//		}
//		int count = 0;
//		char MaxChar;
//		for (int i = 0; i < alphabet.size(); ++i) {
//			int newCount = 0;
//			for (int j = 0; j < str2.length(); ++j) {
//				if (alphabet[i] == str2[j])
//					++newCount;
//			}
//			if (newCount >= count) {
//				MaxChar = alphabet[i];
//				count = newCount;
//			}
//		}
//		cout << endl << "#"<<trial << " : " << count << endl;
//		++trial;
//	}
//
//	return 0;
//}