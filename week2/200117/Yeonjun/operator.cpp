//#include<iostream>
//#include<vector>
//#include<string>
//#include<stack>
//#include <typeinfo>
//using namespace std;
//
//
//int main() {
//	int TestCase, Trial;
//	Trial = 1;
//	cout << "TestCase : ";
//	cin >> TestCase;
//	cout << endl;
//	stack<int> numStack;
//	
//	while (Trial <= TestCase) {
//		int input;
//		while (cin >> input) {
//			if (input == int('+') || input == int('-') || input == '*' || input == '/' || input == '.') {
//				if (numStack.size() < 2) {
//					cout << "error...";
//					break;
//				}
//				else if (input == '.') {
//					cout << "#" <<Trial << " " <<numStack.top() << endl;
//					break;
//				}
//				else {
//					char first, second;
//					int firstInt, secondInt;
//					int total;
//					first = numStack.top();
//					firstInt = first - '0';
//					numStack.pop();
//					second = numStack.top();
//					secondInt = second - '0';
//					numStack.pop();
//
//					if (input == '+') {
//						total = first + second;
//						numStack.push(total);
//					}
//					else if (input == '-') {
//						total = first - second;
//						numStack.push(total);
//					}
//					else if (input == '*') {
//						total = first * second;
//						numStack.push(total);
//					}
//					else if (input == '/') {
//						total = first / second;
//						numStack.push(total);
//					}
//				}
//			}
//			else {
//				numStack.push(int(input));
//			}
//		}
//		Trial++;
//	}
//
//	return 0;
//}