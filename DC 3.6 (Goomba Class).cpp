#include <iostream>
using namespace std;

class Goomba {
private:
	int xpos;
	int ypos;
	bool isAlive;
	char goombaColor;
public:
	Goomba(); // default constructor
	Goomba(int x, int y, char i); //parameterized constructor
	void walk();
	void printInfo();
	void kill();
	void setPosition(int x, int y);
	bool CheckisDead();
};


int main() {
	Goomba Larry(300, 400, 'l');
	Goomba Bob;
	Larry.printInfo();
	Larry.walk();
	Larry.printInfo();
	Larry.setPosition(300, 400);
	Larry.printInfo();
	Larry.kill();
	Larry.printInfo();
	Larry.CheckisDead();
	Bob.printInfo();
	Bob.CheckisDead();
}

Goomba::Goomba() {
	xpos = 0;
	ypos = 0;
	isAlive = false;
	goombaColor = 'b';
}
Goomba::Goomba(int x, int y, char i) {
	xpos = x;
	ypos = y;
	isAlive = true;
	goombaColor = i;
}

void Goomba::walk() { xpos += 1; }

void Goomba::setPosition(int x, int y) {
	xpos = x;
	ypos = y;
	isAlive = true;
}

bool Goomba::CheckisDead() {
	if (isAlive == false) {
		cout << "false" << endl;
		return 0;
	}
	else
		cout << "true" << endl;
		return 1; {
	}
}

void Goomba::kill() {
	isAlive = false;
}

void Goomba::printInfo() {
	cout << "Hi, I'm a goomba and my position is " << xpos << "," << ypos << endl;
	if (isAlive == true)
		cout << "I am currently alive." << endl;
	else
		cout << "I am currently dead." << endl;
	if (goombaColor == 'l')
		cout << "My color is blue" << endl;
	if (goombaColor == 'b')
		cout << "My color is brown" << endl;

}
