#include <iostream>
#include <cmath>
using namespace std;

double area(int k); // area function

class le_fishe {
private:
	string name;
	int foodbar;
	int stamina;
	int health;
public:
	le_fishe();
	le_fishe(string j);
	void eat();
	void print();
	void rest();
	void heal();
};

int main() {
	int h;
	cout << "Enter your radius" << endl;
	cin >> h;
	cout << "The area of your circle is " << area(h) << endl; //area function call

	le_fishe s1("Alex");
	le_fishe s2("Jevin");
	le_fishe s3("Tam");

	char input = 'p';
	while (input != 'q') {
		cout << "Le_Fishes asks you to make their discussions today? (e) to eat food, (r) to rest, or (h) to heal" << endl;
		cin >> input;

		if (input == 'e') {
			s1.eat();
			s2.eat();
			s3.eat();
		}
		if (input == 'r') {
			s1.rest();
			s2.rest();
			s3.rest();
		}
		if (input == 'r') {
			s1.heal();
			s2.heal();
			s3.heal();
			
		}
		s1.print();
		s2.print();
		s3.print();
	}

}
double area(int k) { // area function definition
	double m = 3.14159 * pow(k, 2);
	return (m);
}
le_fishe::le_fishe() { // default settings for le_fishe
	foodbar = 50;
	stamina = 50;
	health = 10;
}
le_fishe::le_fishe(string n) { // 
	foodbar = 50;
	stamina = 50;
	health = 10;
	name = n;
}
void le_fishe::eat() { // eat function definition
	foodbar += 10;
	cout << "Hmm Yummy Borger!" << endl;
}
void le_fishe::print() { // print out status function definition
	cout << name << " status right now: " << endl;
	cout << foodbar << " foodbar" << endl;
	cout << stamina << " stamina" << endl;
	cout << health << " health" << endl;
}
void le_fishe::rest() {
	stamina += 10;
	cout << "Lemme just float here for a couple seconds" << endl;
}
void le_fishe::heal() {
	health += 10;
	cout << "Hold up lemme call up my personal wizard to heal me real quick up" << endl;
}
