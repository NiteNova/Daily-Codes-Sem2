#include <iostream>
using namespace std;

int main() {
	int choice;
	cout << "Songs: (1) - Save Your Tears by The Weeknd, (2) - Notion by The Rare Occasions, (3) - family ties by Baby Keem, (4) - Self Care by Mac Miller " << endl;
	cout << "Enter Song Choice: " << endl;
	cin >> choice;

	switch (choice) {
	case 1:
		cout << "Take me back 'cause I wanna stay, Save your tears for another, Save your tears for another day" << endl;
		break;
	case 2:
		cout << "Oh, back when I was younger, was told by other youngsters. That my end will be torture beneath the earth" << endl;
		break;
	case 3:
		cout << "Chopper doing circles, it's a Vert', Vert' . Take him to the party, he's a nerd (pop out)" << endl;
		break;
	case 4:
		cout << "I switched the time zone, but what do I know? Spendin' nights hitchhikin', where will I go ? " << endl;
		break;
	default:
		cout << "Sorry, not an option" << endl;

		}
}
