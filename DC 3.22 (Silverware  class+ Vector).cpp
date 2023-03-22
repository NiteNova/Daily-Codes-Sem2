#include <iostream>
#include<vector>
using namespace std;

class cutler {

private:
	enum {Fork, Spoon, Knife};
	bool isClean;
	int type;

public:
	cutler();
	void printInfo();
	void use();
	void wash();

};


int main(){
	vector<cutler*>c;
	vector<cutler*>::iterator iter;

	srand(time(NULL));
	for (int i = 0; i < 2; i++) {
		cutler* newc = new cutler();
		c.push_back(newc);
	}

	for (iter = c.begin(); iter != c.end(); iter++) {
		(*iter)->printInfo();
		(*iter)->use();
		(*iter)->printInfo();
		(*iter)->wash();
		(*iter)->printInfo();
		cout << endl;
	}
	
}

cutler::cutler() {
	isClean = true;
	type = rand() % 3;
}

void cutler::printInfo() {
	if (type == Fork) {
		cout << "Fork" << endl;
	}
	else if (type == Spoon) {
		cout << "Spoon" << endl;

	}
	else
		cout << "Knife" << endl;

	if (isClean == true) {
		cout << "Your silverware is clean" << endl;
	}
	else
		cout << "Youre silverware is dirty" << endl;

}

void cutler::use() {
	isClean = false;
}
void cutler::wash() {
	isClean = true;
}
