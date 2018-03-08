#include <vector>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <stdio.h>

/* TEMPLATE FUNCTIONS */
template <class T>
void printVect(std::vector<T> v) {
	for (T vi : v) {
		std::cout << vi << " ";
	}
	std::cout << std::endl;
}

/* DYNAMIC PROGRAMMING */
// When you need to hash something to a memo, stringify

// Ex: the making change subproblem
std::string stringify(long n, std::vector<long> v) {
	std::string s = std::to_string(n) + ".";
	for (long vi : v) {
		s += std::to_string(vi);
	}
	return s;
}

int main(int argc, char const *argv[]) {

	/* IO */
	std::cout << "My name is milo" << std::endl;

	/* VECTORS: compile with -std=c++11 */
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

	/* HASHING */
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

	// Iterating through pairs
	for (std::pair<int, int> p : m) {
		std::cout << p.first << " " << p.second << std::endl;
	}

	m.clear(); // Destroys all items in the map

	/* String: zero-indexed */
	std::string s = "My name is milo";

	// replacing a single char
	s[11] = 'x'; // must use single quotes for char
	std::cout << s << std::endl;

	std::string repl = s; // copy

	// Replace(start_index, length, string_to_insert)
	repl.replace(11, 4, "sdf;lkksdflkj");
	std::cout << repl << std::endl;

	// Testing vector slice
	std::vector<std::string> strs = {"a", "b", "c"};

	std::vector<std::string> v1(&strs[0], &strs[1+1]);
	printVect(v1);

	// Make a 2D array
	int array[2][10];
	array[0][0] = 1000;
	std::cout << array[0][0] << std::endl;

	// Trying out some standard libs
	std::stack<int> stack;
	stack.push(10);
	stack.top();
	stack.pop();

	std::queue<int> queue;
	queue.push(10);
	queue.push(20);
	queue.front();
	queue.pop();
	queue.back();

	std::unordered_map<int, std::string> umap;
	umap[5] = "five";
	std::string lookup = umap[5];
	std::cout << lookup << std::endl;

	if (umap.find(5) != umap.end()) {
		std::cout << umap[5] << std::endl;
	}

	std::unordered_set<std::string> uset;
	uset.insert("magnus");
	uset.insert("diabetes");

	for (auto key : uset) {
		std::cout << key << std::endl;
	}

	if (uset.find("windows98") != uset.end()) {
		std::cout << "Found windows98" << std::endl;
	} else {std::cout << "not found" << std::endl; }

	return 0;
}