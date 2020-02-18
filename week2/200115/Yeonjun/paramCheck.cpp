//#include<iostream>
//#include<vector>
//#include<string>
//#include<fstream>
//using namespace std;
//
//void pop(vector<char>& vec, char paren) {
//	char popValue = vec[vec.size() - 1];
//	if (paren == ']') {
//		if (popValue == '[')
//			vec.pop_back();
//	}
//	else if (paren == '}') {
//		if (popValue == '{')
//			vec.pop_back();
//	}
//	else if (paren == ')') {
//		if (popValue == '(')
//			vec.pop_back();
//	}
//}
//
//int main() {
//	int TestCase;
//	int Trial = 1;
//	cout << "TestCase : ";
//	cin >> TestCase;
//	while (Trial <= TestCase) {
//		string param;
//		cout << "\nparenthesis : ";
//		cin >> param;
//
//		int length = param.length();
//		vector<char>* stack = new vector<char>;
//
//		for (int i = 0; i < length; ++i) {
//			if (param[i] == '[' || param[i] == '{' || param[i] == '(') {
//				stack->push_back(param[i]);
//			}
//			else if (param[i] == ']' || param[i] == '}' || param[i] == ')') {
//				if (param[i] == ']') {
//					pop(*stack, ']');
//				}
//				else if (param[i] == '}') {
//					pop(*stack, '}');
//				}
//				else if (param[i] == ')') {
//					pop(*stack, ')');
//				}
//			}
//		}
//		if (stack->size() == 0)
//			cout << "1" << endl;
//		else if (stack->size() > 0)
//			cout << "0" << endl;
//
//		delete stack;
//		++Trial;
//	}
//
//	return 0;
//}