/* All things const */
#include <iostream>

void constPermutations() {

	// Read declarations from right to left.
	int myInt = 13;

	const int myConstInt = 12;

	int * ptrToInt;

	int * const constPtrToInt = &myInt; // Note: this must be initialized right away, since it never can be again.

	const int intThatIsConst = 14; // This also has to be assigned right away.

	const int* ptrToIntThatIsConst;
	ptrToIntThatIsConst = &myInt;

	// For some reason, a pointer to an int that is const can still be pointed at
	// a non-const int. Below I can change the int and the pointer will reflect
	// the new value...
	std::cout << "ptrToIntThatIsConst: " << *ptrToIntThatIsConst << std::endl;
	myInt = 2;
	std::cout << "ptrToIntThatIsConst: " << *ptrToIntThatIsConst << std::endl;

	// Similarly, this is allowed to be assigned to a non-const int...
	const int * const constPtrToIntThatIsConst = &myInt;
}

struct Example {

	/* Const functions do not allow any modification of the object they are from. */
	int getATimesB() const {
		// If I try to do the following, c++ complains that "a" is a read-only member.
		// a = 4;
		return a * b;
	}

	/* This member is non-const, so it cannot be called from a const instance of Example. */
	void printMembers() {
		std::cout << a << " " << b << std::endl;
	}

	int a = 2;
	int b = 3;
};

int main(int argc, char const *argv[])
{
	// Create a non-const instance of Example.
	Example* example = new Example();
	example->printMembers();

	// Use the const member function.
	std::cout << example->getATimesB() << std::endl;

	// Create a const instance of Example.
	const Example exampleConst;

	// When I try to call a non-const member function on a const instance of the struct
	// below, it will throw an error.
	// error: passing ‘const Example’ as ‘this’ argument discards qualifiers
	// exampleConst.printMembers();

	// Create a pointer to a const Example instance.
	Example const * exampleConstPtr = new Example(); // This is allowed because the method is const.
	int result = exampleConstPtr->getATimesB();
	std::cout << "Can call a const method: " << result << std::endl;

	// This is not allowed because printMembers is non-const.
	// exampleConstPtr->printMembers();
	delete example;

	constPermutations();

	return 0;
}
