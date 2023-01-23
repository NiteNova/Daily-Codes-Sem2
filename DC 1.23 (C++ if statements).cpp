#include <iostream>
using namespace std;

int main() {

	int userinput;

	cout << "Enter the your age " << endl;
	cin >> userinput;
	if (userinput <= 12)
		cout << "You're too young to play this game" << endl;
	else if (userinput >= 13 && userinput <= 17)
		cout << "You need guardian permission in order to play this game" << endl;
	else
		cout << "Welcome to the game!" << endl;

	char animal;

	cout << "What is your favorite animals 'd' for dog 'c' for cat 'b' for birb" << endl;
	cin >> animal;
	if (animal == 'd')
		cout << "woof woof" << endl;
	else if (animal == 'c')
		cout << "meow meow" << endl;
	else if (animal == 'b')
		cout << "CAW CAW" << endl;
	else
		cout << "RAWR!!!!!!" << endl;
}
