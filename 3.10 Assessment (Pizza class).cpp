#include <iostream>
using namespace std;

class Pizza {
private:
	int toppings;
	float price;
	bool isBaked;
public:
	Pizza();
	void printInfo();
	int addTopping();
	float calcPrice();
	void bake();
};

int main() {
	Pizza r;
	Pizza i;
	Pizza g;

	r.addTopping();
	r.bake();

	
	i.addTopping();

	g.addTopping();
	g.bake();


	//I call the calcprice inside printinfo
	cout << endl;
	r.printInfo();
	cout << endl;
	i.printInfo();
	cout << endl;
	g.printInfo();

}

Pizza::Pizza() {
	toppings = 0;
	price = 0;
	isBaked = false;
}
void Pizza::bake() {
	isBaked = true;
}


int Pizza::addTopping() {
	int amount;
	cout << "How much toppings do you want?: ";
	cin >> amount;
	toppings = amount;
	return toppings;
}

float Pizza::calcPrice() {
	price = (toppings * 2 + 10);
	return price;
}

void Pizza::printInfo() {
	cout << "I have: " << toppings << " toppings" << endl;
	if (isBaked == false)
		cout << "I am not a baked pizza" << endl;
	else
		cout << "I am a baked pizza" << endl;
	calcPrice();
	cout << "The price of me is: "<< price << endl;
}
