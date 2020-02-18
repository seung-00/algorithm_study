#include<iostream>
#include<vector>
using namespace std;

struct linkedNode {
	linkedNode* next;
	int data;
};

class LinkedList {
public:
	LinkedList() {};

	linkedNode* getNext() {
		curPtr = curPtr->next;
		++curLoc;
		return curPtr;
	}
	linkedNode* getCurNode() {
		return curPtr;
	}
	void resetPtr() {
		curPtr = header;
		curLoc = 0;
	}

	void addNodes(int* arr, int length) {
		if (this->length == 0) {
			for (int i = 0; i < length; i++) {
				linkedNode* newNode = new linkedNode;
				newNode->data = *(arr + i);
				if (i == 0) {
					header = newNode;
					curPtr = header;
				}
				else {
					curPtr->next = newNode;
					getNext();
				}
			}
			this->length = length;
			return;
		}
		resetPtr(); 
		for (int i = 1; i < this->length; ++i) {
			if (*arr >= getCurNode()->data) {
				linkedNode* temp = getCurNode()->next;
				for (int j = 0; j < length; j++) {
					linkedNode* newNode = new linkedNode;
					newNode->data = *(arr + j);
					if (j == length - 1) {
						getCurNode()->next = newNode;
						newNode->next = temp;
					}
					else {
						getCurNode()->next = newNode;
						getNext();
					}
				}
				this->length = length;
				return;
			}
			if (i == length - 1) {
				if (*arr >= getCurNode()->data) {
					for (int j = 0; j < length; j++) {
						linkedNode* newNode = new linkedNode;
						newNode->data = *(arr + j);
						curPtr->next = newNode;
						getNext();
					}
					this->length = length;
					return;
				}
			}
			if (i == 1) {
				if (*arr <= getCurNode()->data) {
					linkedNode* temp = curPtr;
					for (int j = 0; j < length; j++) {
						linkedNode* newNode = new linkedNode;
						newNode->data = *(arr + j);
						if (j == 0) {
							header = newNode;
							curPtr->next = newNode;
						}
						else if (j == length - 1) {
							curPtr->next = temp;
						}
						else {
							curPtr->next = newNode;
							getNext();
						}
					}
					this->length = length;
					return;
				}
			}
			getNext();
		}
	}

	int getLength() {
		return length;
	}
	void printNodes() {
		resetPtr();
		vector<int> vec;
		for (int i = 0; i < this->length; i++) {
			vec.push_back(curPtr->data);
			getNext();
		}
		for (int i = 0; i < this->length; i++) {
			cout << vec.back() << " ";
			vec.pop_back();
		}
		cout << endl;
	}

private:
	linkedNode* curPtr = nullptr;
	linkedNode* header = nullptr;
	int length = 0;
	int curLoc = 0;
};


int main() {
	int TestCase;
	int Trial = 1;
	cout << "TestCase : ";
	cin >> TestCase;
	while (Trial <= TestCase) {
		int seqLength, seqCount;
		cin >> seqLength >> seqCount;
		int count = 1;
		int getNum = 0;
		int* arr = new int[seqLength*seqCount];
		LinkedList list;
		for (int i = 0; i < seqCount; i++) {
			for (int j = 0; j < seqLength; j++) {
				cin >> getNum;
				arr[i+j] = getNum;
				if (j == seqLength- 1)
					list.addNodes(&arr[count - seqLength], seqLength);
				++count;
			}
		}
		list.printNodes();

		delete[] arr;
		++Trial;
	}

	return 0;
}