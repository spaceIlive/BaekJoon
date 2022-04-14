#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string str;
	int num;
	int idx;
	int leng;
	cin >> str;
	cin >> num;
	idx = str.length();
	leng = idx;
	cin.ignore();
	for (int i = 0; i < num; i++) {
		string cmd;
		cin >> cmd;
		if (cmd == "P") {
			string x;
			cin >> x;
			str.insert(idx, x);
			idx += 1;
			leng += 1;

		}
		else if (cmd == "L") {
			if (idx > 0) {
				idx -= 1;
			}
		}
		else if (cmd == "D") {
			if (idx < leng) {
				idx += 1;
			}
		}
		else if (cmd == "B") {
			if (idx > 0) {
				str.erase(((idx)-1) , 1);
				idx -= 1;
				leng -= 1;
			}
		}
	}
	cout << str;

	return 0;
}