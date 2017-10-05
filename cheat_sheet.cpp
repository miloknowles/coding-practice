#include <vector>
#include <iostream>



int main(int argc, char const *argv[]) {

	// IO stuff

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

	return 0;
}


