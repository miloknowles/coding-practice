#include <vector>
#include <iostream>
#include <unordered_map>


int main(int argc, char const *argv[]) {

	// IO stuff
	std::cout << "My name is milo" << std::endl;

	// Vectors: compile with -std=c++11
	std::vector<int> vect = {1, 2, 3, 4, 5, 6, 7, 8};
	vect.push_back(9);
	vect.pop_back();
	vect.back();
	vect.front();

	for (int i : vect) {
		std::cout << i << std::endl;
	}

	for (auto it = begin(vect); it != end(vect); it++) {
		std::cout << *it << std::endl;
	}

	// Hashing
	std::unordered_map<int, int> m;
	m[1] = 10;
	m[2] = 20;
	m[3] = 30;

	// Check existence of a key
	if (m.find(3) != m.end()) {
		std::cout << "Found the key" << std::endl;
	}

	// Iterating through keys
	for (std::unordered_map<int, int>::iterator it = m.begin(); it != m.end(); ++it) {
		std::cout << "Key: " << it->first << " Value: " << m[it->first] << std::endl;
	}

	return 0;
}


