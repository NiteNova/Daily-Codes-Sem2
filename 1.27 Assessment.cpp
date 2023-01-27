#include<iostream>
using namespace std;

int main() {
	// Nested for loops
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 1; j++) {
			for (int j = 2; j < 5; j++) {

				cout << j << " ";
			}
		}
		cout << endl;
	}

	cout << endl;

	int cookies; // First to If statements

	cout << "Ayo, how many cookies u got in that bag??!" << endl;
	cin >> cookies;

	if (cookies < 5)
		cout << "broo thats like not enough cookies, if u want I could give you an extra one." << endl;
	else if (cookies < 10)
		cout << "Yo thats a good amount of cookies you got there." << endl;
	else
		cout << "DANGG, Bro thats like too much cookies gimme one." << endl;

	cout << endl; // Second part to If statements

	char character;

	cout << "Yo whats your favorite character?: (b) for bart simpson, (s) for scooby doo, (r) for rick sanchez, or (d) for daffy duck, or (p) for Patrick Star" << endl;
	cin >> character;

	if (character == 'b')
		cout << "Eat my shorts" << endl;
	else if (character == 's')
		cout << "Scooby dooby doo" << endl;
	else if (character == 'r')
		cout << "Wubba Lubba dub dub" << endl;
	else if (character == 'd')
		cout << "Sufferin' succotash!" << endl;
	else if (character == 'p')
		cout << "The inner machinations of my mind are an enigma" << endl;

	cout << endl; // Switch statements

	cout << "Yo whats your favorite character?: (b) for bart simpson, (s) for scooby doo, (r) for rick sanchez, or (d) for daffy duck, or (p) for Patrick Star" << endl;
	cin >> character;

	switch (character) {
	case 'b':
		cout << "Eat my shorts" << endl;
		break;
	case 's':
		cout << "Scooby dooby doo" << endl;
		break;
	case 'r':
		cout << "Wubba Lubba dub dub" << endl;
		break;
	case 'd':
		cout << "Sufferin' succotash!" << endl;
		break;
	case 'p':
		cout << "The inner machinations of my mind are an enigma" << endl;
		break;
	}

	cout << endl; // Nested If statements

	char choice;
	char choice2;

	cout << "Do you want ice cream (i) or candy (c)?" << endl;
	cin >> choice;
	cout << "Do you want chocolate (c) or fruit (f)?" << endl;
	cin >> choice2;

	if (choice == 'i')
		if (choice2 == 'c')
			cout << "You're getting a hot fudge sundae" << endl;
		else if (choice2 == 'f')
			cout << "You're getting a strawberry blizzard" << endl;
	if (choice == 'c')
		if (choice2 == 'c')
			cout << "You're getting a hershey bar" << endl;
		else if (choice2 == 'f')
			cout << "You're getting starbursts" << endl;
}
