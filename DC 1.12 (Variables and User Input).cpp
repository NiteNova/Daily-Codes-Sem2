#include <iostream>
using namespace std;

int main() {
	char f_int;
	char l_int;
	cout << "What is your first inital?" << endl;
	cin >> f_int;
	cout << "What is your last inital?" << endl;
	cin >> l_int;
	cout << "First Initial: " << f_int << " Last Initial: " << l_int << endl;

	int money;
	cout << "How much money do you have" << endl; 
	cin >> money; 
	cout << "You have: " << money << " dollars" << endl;

	int id;
	cout << "What's your school id?: " << endl;
	cin >> id;
	cout << "Your school id is " << id << endl;
}
