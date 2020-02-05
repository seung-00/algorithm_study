//#include<iostream>
//#include<vector>
//#include<string>
//using namespace std;
//
//void DelDuplicate(vector<char>& stack, string letters) {
//	int length = letters.length();
//
//	for (int i = 0; i < length; i++) {
//		if (i == 0 || stack.size() == 0)
//			stack.push_back(letters[i]);
//		else {
//			int stackTop = stack[stack.size() - 1];
//			if (stackTop == letters[i])
//				stack.pop_back();
//			else
//				stack.push_back(letters[i]);
//		}
//	}
//
//}
//
//int main() {
//	int TestCase;
//	int Trial = 0;
//	cout << "Case : ";
//	cin >> TestCase;
//	while (Trial <= TestCase) {
//		string letters;
//		cout << "String : ";
//		cin >> letters;
//		vector<char> stack;
//		
//		DelDuplicate(stack, letters);
//		
//		int newLength = stack.size();
//		cout << endl;
//
//		for (int i = 0; i < newLength; i++) {
//			cout << stack[i];
//		}
//		cout << endl;
//		
//		++Trial;
//	}
//
//	return 0;
//}