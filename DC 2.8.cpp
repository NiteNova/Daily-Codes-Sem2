#include<iostream>
#include<array>
using namespace std;

void print_greeting();//declaration
void print_gestures();
int input_throw(string thrower, string opponent);
int calc_winner(int t1, int t2);

string gestures[] = { "Rock", "Paper", "Scissors", "Lizard", "Spock" };
int winloss[5][5] = { {2, 0, 1, 1, 0},
 {1, 2, 0, 0, 1},
 {0, 1, 2, 1, 0},
 {0, 1, 0, 2, 1},
 {1, 0, 1, 0, 2} };//keep going

int main() {
	string name1;
	string name2;

	//type winloss matrix here

	print_greeting();

	cout << "Enter player 1's name: ";
	cin >> name1;
	cout << "Enter player 2's name: ";
	cin >> name2;

	int throw1 = input_throw(name1, name2);
	int throw2 = input_throw(name2, name1);

	int winner = calc_winner(throw1, throw2);

	while (winner == 2) {
		cout << "It's a tie; both players will throw again." << endl;
		int throw1 = input_throw(name1, name2);
		int throw2 = input_throw(name2, name1);
		winner = calc_winner(throw1, throw2);
	}

	if (winner == 1) {
		cout << gestures[throw1] << " defeats " << gestures[throw2] + "." << endl;
		cout << name1 << "defeats" << name2 + "." << endl;
	}
	else {
		cout << gestures[throw2] << " defeats " << gestures[throw1] + "." << endl;
		cout << name2 << " defeats " << name1 + "." << endl;
	}
}

void print_greeting() {
	cout << "Welcome to Rock-Paper-Scissors-Lizard-Spock!" << endl;
	//actually put stuff here
}

void print_gestures() {
	cout << "Choices are:" << endl;
	cout << "(0) Rock, (1) Paper, (2) Scissors, (3) Lizard, (4) Spock" << endl;
}
//do the definition for print gestures here
int input_throw(string thrower, string opponent) {
	int the_throw;
	cout << "It is" << thrower << "'s turn." << endl;
	print_gestures();
	cout << "no peeking, " << opponent << endl;
	cout << thrower << ", what is your throw" << endl;
	cin >> the_throw;

	while (the_throw < 0 || the_throw >= sizeof(gestures))
		cout << "Invalid choice: Try again." << endl;
	cout << thrower << ", what is your throw" << endl;
	cin >> the_throw;
	cout << thrower << " throws " << gestures[the_throw] << "." << endl;
	return the_throw;
}
int calc_winner(int t1, int t2) {
	return winloss[t1][t2];
}
