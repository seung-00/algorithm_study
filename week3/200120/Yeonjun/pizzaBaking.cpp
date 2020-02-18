//#include<iostream>
//#include<queue>
//#include<vector>
//#include<string>
//using namespace std;
//
//int main() {
//	int TestCase;
//	int	Trial = 1;
//	cin >> TestCase;
//	while (Trial <= TestCase) {
//		int ovenSize, pizza;
//		cin >> ovenSize >> pizza;
//		int cheese;
//		queue<pair<int, int>>oven;
//		vector<int>pizzaCheese;
//		int count = 0;
//		int finalPizza = 0;
//		for (int i = 0; i < pizza; i++) {
//			cin >> cheese;
//			pizzaCheese.push_back(cheese);
//		}
//		for (int i = 0; i < ovenSize; i++) {
//			oven.push(pair<int,int>(pizzaCheese[i], 0));
//			++count;
//		}
//		
//		while (oven.empty() != 1 && count <= pizza) {
//			if (oven.size() == 1 && count == pizza) {
//				finalPizza = oven.front().first;
//				break;
//			}
//			if (oven.front().second / 2 == 0) {
//				oven.pop();
//				if (count != pizza) {
//					oven.push(pair<int, int>(pizzaCheese[count], pizzaCheese[count]));
//					count++;
//				}
//			}
//			else if(oven.front().second / 2 !=  0){
//				int temp = oven.front().first;
//				int temp2 = oven.front().second / 2;
//				oven.pop();
//				oven.push(pair<int, int>(temp, temp2));
//			}
//		}
//		for (int i = 0; i < pizza; i++) {
//			if (pizzaCheese[i] == finalPizza) {
//				cout << "#" << Trial << " " << i + 1 << endl;
//				break;
//			}
//		}
//		++Trial;
//	}
//	return 0;
//}