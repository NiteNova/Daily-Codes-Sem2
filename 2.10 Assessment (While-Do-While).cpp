#include <iostream>
using namespace std;
// Don't forget to grade for my understanding on if, nested if, functions from last week of 2/10
// Only thing you needed from me on this quiz was the while and do while loops


int main() {
	int lol = 1; 
	while (lol <= 34) {
		cout << lol << endl; 
		(lol += 5);
	}

	cout << endl;

	bool donut = false;
	char user;
	while (donut != true) {
		cout << "DONUT! you want another donut?1 " << endl;
		cin >> user;
		if (user == 'y')
			cout << "DONUT!" << endl;
		else
			donut = true;
	}

	cout << endl;

	int donut1 = false;
	char user1;
	do {
		cout << "DONUT! you want another donut?2 " << endl;
		cin >> user1;
		if (user1 == 'y')
			cout << "DONUT!" << endl;
		else
			donut1 = true;
	} 
	while (donut1 != true);
}
