#include <iostream>
using namespace std;

class planet {
private:
		float mass;
		int moons;
		int rings;
		char category;
		bool hasLife;
public:
		planet();
		planet(int s, int m, int r, char c, bool h);
		void printinfo();
		void captureMoon();
		void shredMoon();
		void growLife();
		void getHitByAsteroid();
};

int main() {
	planet earth;
	cout << "EARTH" << endl;
	earth.printinfo();

	earth.getHitByAsteroid();
	earth.shredMoon();
	earth.printinfo();

	cout << endl;
	cout << "MARS" << endl;
	planet mars(6.39, 2, 0, 'r', false);
	mars.printinfo();
  
	mars.growLife();
	mars.captureMoon();
	mars.printinfo();
  
	cout << endl;
	cout << "VENUS" << endl;
	planet venus(4.867, 0, 0, 'r', false);
	venus.printinfo();
	venus.captureMoon();
	venus.shredMoon();
	venus.printinfo();
	
}


planet::planet() {
	mass = 5.97219;
	moons = 1;
	rings = 0;
	category = 'r';
	hasLife = true;
}

planet::planet(int s, int m, int r, char c, bool h) {
	mass = s;
	moons = m;
	rings = r;
	category = c;
	hasLife = h;
}

void planet::printinfo() {
	cout << "My mass is " << mass << " 10^24 in kg." << endl;
	cout << "I have " << moons << " moons." << endl;
	cout << "I have " << rings << " rings." << endl;
	if (category == 'r')
		cout << "I'm a rocky planet." << endl;
	else if (category == 'i')
		cout << "I'm a icy planet." << endl;
	else if (category == 'g')
		cout << "I'm pretty gassy." << endl;
	if (hasLife == true)
		cout << "I have the lifes." << endl;
	else
		cout << "Dang I have no ones." << endl;
}

void planet::captureMoon() {
	moons += 1;
}

void planet::shredMoon() {
	rings += 1;
}

void planet::growLife() {
	hasLife = true;
}

void planet::getHitByAsteroid() {
	hasLife = false;
}
