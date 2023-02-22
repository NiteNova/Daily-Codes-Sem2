#include <iostream>
using namespace std;


int MonsterGen(char biome);


int main() {
	int room = 1;
	int hp = 100;
	char choice;

	cout << "Welcome to the text based game!" << endl;
	do {
		switch (room) {
		case 1:
			hp -= MonsterGen('r'); //river
			cout << hp << endl;
			cout << "You are in room 1. You can go (e)ast." << endl;
			cin >> choice;
			if (choice == 'e')
				room = 2;
			else
				cout << "Error." << endl;
			break;
		case 2:
			hp -= MonsterGen('d'); //desert
			cout << hp << endl;
			cout << "You are in room 2. You can go (w)est or (s)outh." << endl;
			cin >> choice;
			if (choice == 'w')
				room = 1;
			else if (choice == 's')
				room = 3;
			else
				cout << "Error." << endl;
			break;
		case 3:
			hp -= MonsterGen('s'); // swamp
			cout << hp << endl;
			cout << "You are in room 3. You can go (n)orth or (s)outh)." << endl;
			cin >> choice;
			if (choice == 'n')
				room = 2;
			else if (choice == 's')
				room = 4;
			else
				cout << "Error." << endl;
			break;
		case 4:
			hp -= MonsterGen('d'); // dripstone cave
			cout << hp << endl;
			cout << "You are in room 4. You can go (n)orth." << endl;
			cin >> choice;
			if (choice == 'n')
				room = 3;
			else
				cout << "Error." << endl;
			break;

		}
	} while (choice != 'q');
}

int MonsterGen(char biome) {
	int num = rand() % 100;
	if (biome == 'r') { //river
		if (num < 10) {
			cout << "A spider appears" << endl;
			return 5;
		}
		else if (num < 50) {
			cout << "A drowned appears" << endl;
			return 10;
		}
		else if (num < 85) {
			cout << "A skeleton attacks" << endl;
			return 10;
		}
		else if (num < 90) {
			cout << "A witch attacks" << endl;
			return 15;
		}
		else {
			cout << "No monster, you're safe this turn" << endl;
			return 0;
		}
	}
	if (biome == 'd') { //desert
		if (num < 30) {
			cout << "A spider appears" << endl;
			return 5;
		}
		else if (num < 50) {
			cout << "A zombie appears" << endl;
			return 10;
		}
		else if (num < 70) {
			cout << "A skeleton attacks" << endl;
			return 10;
		}
		else if (num < 90) {
			cout << "A husk attacks" << endl;
			return 15;
		}
		else {
			cout << "No monster, you're safe this turn" << endl;
			return 0;
		}
	}
	if (biome == 's') { //swamp
		if (num < 10) {
			cout << "A spider appears" << endl;
			return 5;
		}
		else if (num < 30) {
			cout << "A zombie appears" << endl;
			return 10;
		}
		else if (num < 50) {
			cout << "A creeper attacks" << endl;
			return 15;
		}
		else if (num < 90) {
			cout << "A witch attacks" << endl;
			return 15;
		}
		else {
			cout << "No monster, you're safe this turn" << endl;
			return 0;
		}
	}
	if (biome == 'd') { //swamp
		if (num < 20) {
			cout << "A spider appears" << endl;
			return 5;
		}
		else if (num < 40) {
			cout << "A zombie appears" << endl;
			return 10;
		}
		else if (num < 60) {
			cout << "A creeper attacks" << endl;
			return 15;
		}
		else if (num < 80) {
			cout << "An enderman attacks" << endl;
			return 15;
		}
		else {
			cout << "No monster, you're safe this turn" << endl;
			return 0;
		}
	}
}
