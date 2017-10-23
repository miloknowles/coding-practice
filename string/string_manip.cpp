#include <iostream>
#include <cctype>
#include <string>

void deleteStr(std::string& input, std::string delstr) {
	while (input.find(delstr) != -1) {
		input.replace(input.find(delstr), delstr.length(), "");
	}
}

int main(int argc, char const *argv[])
{
	std::string me = "milo knowles";
	std::cout << me << std::endl;

	// Convert uppercase
	std::string me_upper;
	for (char c : me) {
		me_upper += toupper(c);
	}
	std::cout << me_upper << std::endl;

	// Convert lowercase
	std::string me_lower;
	for (char c : me_upper) {
		me_lower += tolower(c);
	}
	std::cout << me_lower << std::endl;

	// Finding
	// Find gives the index of the first character in the matched phrase
	int loc0 = me.find("milo");
	int loc1 = me.find("ilo");
	int loc4 = me.find(" ");
	int loc_dne = me.find("knowls"); // returns -1

	std::cout << loc0 << std::endl;
	std::cout << loc1 << std::endl;
	std::cout << loc4 << std::endl;
	std::cout << loc_dne << std::endl;

	// Reverse finding
	int loc_o = me.rfind("o"); // finds the last occurence of 'o'
	std::cout << loc_o << std::endl;

	// Find first of
	std::string random = "m1l0 kn0wl3s";
	int loc = random.find_first_of("123456789"); // expect 1
	std::cout << loc << std::endl;
	loc_dne = random.find_first_of("!@#$^&"); // expect -1
	std::cout << loc_dne << std::endl;

	// Find first not of
	int loc_not = me.find_first_not_of("milo"); // expect 4 (space)
	std::cout << loc_not << std::endl;

	// Substrings
	std::string milo = me.substr(0, 4);
	std::cout << milo << std::endl;

	// Replace
	std::string sentence = "My name is _ and fuck this";
	sentence.replace(11, 1, milo);
	std::cout << sentence << std::endl;

	std::string knowles = me.substr(5); // goes until end of string
	std::cout << knowles << std::endl;

	// Try the delete function
	deleteStr(me, "l");
	std::cout << me << std::endl;

	// Inserting to string
	std::string incomp = "uck this";
	incomp.insert(0, "f");
	std::cout << incomp << std::endl;

	return 0;
}