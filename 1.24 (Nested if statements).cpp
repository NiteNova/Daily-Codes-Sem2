#include<iostream>
using namespace std;

int main() {

	char input1;
	int input2;


	cout << "Do you like platformers? (y/n)" << endl;
	cin >> input1;
	cout << "On a scale of 1-10, how difficult of a game would you like to play?" << endl;
	cin >> input2;

	if (input1 == 'y') {
		if (input2 >= 5)
			cout << "I reccomend Mario!" << endl;
		else if (input2 < 5)
			cout << "I reccomentd Kirby" << endl;
	}
	else if (input1 == 'n') {
		if (input2 >= 5)
			cout << " I reccoment Dark souls" << endl;
		else if (input2 < 5)
			cout << "I reccomend Minecraft" << endl;
	}
	else
		cout << "Sorry, thats not an answer I understand." << endl;
}
