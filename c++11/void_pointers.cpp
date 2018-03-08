#include <string>
#include <iostream>
#include <vector>

int main(int argc, char const *argv[]) {
	std::cout << "Test" << std::endl;

	/* VOID POINTERS: a ptr that can point to any kind of object! */
	void *ptr;

	// Below, the ptr can be assigned to a reference to any of the following objects.
	int myInt = 6;
	float myFloat = 6.7;
	std::vector<int> myVect = {1, 2, 3, 4}; // Note: brace initializer only allowed in c++11.

	struct MyStruct {
		MyStruct() {
			std::cout << "Initalialized MyStruct" << std::endl;
		}
		int value = 6; // Note: non-static initializer only allowed in c++11.
	};

	MyStruct msinstance;

	// All of these are allowed, however the void pointer must be cast to
	// an actual type before it can be dereferenced.
	ptr = &myInt;
	ptr = &myFloat;
	ptr = &myVect;
	ptr = &msinstance;

	ptr = &myInt;
	int* intPtr = static_cast<int*>(ptr);
	std::cout << "Dereferenced intPtr: " << *intPtr << std::endl;

	ptr = &msinstance;
	MyStruct* structPtr = static_cast<MyStruct*>(ptr);
	std::cout << "Dereferenced structPtr: " << structPtr->value << std::endl;

	/* CONST VOID POINTERS */
	//const void pointers only allow you to cast them into const pointers.
	// This is allowed:
	const void* constVoidPtr = &myInt;
	const int* constIntPtr = static_cast<const int*>(constVoidPtr);
	std::cout << "Dereferenced constIntPtr: " << *constIntPtr << std::endl;

	// This is not allowed:
	// int* normalIntPtr = static_cast<int*>(constVoidPtr);
	// std::cout << "Dereferenced normalIntPtr: " << *normalIntPtr << std::endl;
	// error: static_cast from type ‘const void*’ to type ‘int*’ casts away qualifiers

	return 0;
}
