// Playing around with classes in C++

/*

Private inheritance: "HAS-A" relationship
- all public/protected members of the base class become private members of derived class
- private members of base class NOT accessible
- private inheritance provides the functionality of the base class, but NOT the interface
- pretty much equivalent to composition (simply using an instance of the base class as a private member),
  EXCEPT that private inheritance gives the derived class access to protected members of the base class
  whereas composition does not

Public inheritance: "IS-A" relationship
- gives derived class access to the public and protected members of base class
- still no private access to base class
- provides access to the interface of the base class

Protected Inheritance:
- public and protected members of the base class become protected members of derived
- keeps functionality of base class, but hides the interface to it
- allows further derived classes access to the original base class implementation
- "grandchildren are given details about grandparent"

*/


#include <iostream>
#include <string>

// Define everything inside the class declaration (compiler will make this inline)
class MyClass {
private:
	int val;
	std::string str;
public:
	MyClass(int v, std::string s) : val(v), str(s) {
		std::cout << "Created instance of MyClass inline" << std::endl;
	}
};

class SpreadOut {
private:
	int val;
	std::string str;
public:
	SpreadOut(int v, std::string s);
	void reciteBeeMovieScript(const std::string&);
};

// Define the constructor outside of class declaration.
SpreadOut::SpreadOut(int v, std::string s) : val(v), str(s) {
	std::cout << "Created an instance of SpreadOut class" << std::endl;
};
// Define another member function outside of the class.
void SpreadOut::reciteBeeMovieScript(const std::string& script) {
	std::cout << script << std::endl;
}


class DefaultConstructorTest {
public:
	DefaultConstructorTest() {std::cout << "Called default constructor..." << std::endl; }
	DefaultConstructorTest(const std::string& message) { std::cout << message << std::endl; }
};

class InitializerListTest {
private:
	DefaultConstructorTest privateMember;
public:
	InitializerListTest() {}
	InitializerListTest(bool useInitializerList) : privateMember("My default constructor was not called") {}
};


// Overloading operators
class OverloaderPlus {
public:
	void operator + (const OverloaderPlus&) {
		std::cout << "Using the overriden addition operator" << std::endl;
	}
};

// Using the "this" keyword
class TestThisKeyword {
public:
	void isThisMe(const TestThisKeyword& other) {
		if (this == &other) { std::cout << "You passed me into myself" << std::endl; }
		else { std::cout << "This is someone else" << std::endl; }
	}
};

// Inheritance stuff

// This base class has some private and public methods
class BaseClass {
private:
	int privateId;
	void privateMethod() { std::cout << "Called private method of BaseClass" << std::endl; }
public:
	int publicId;
	void publicMethod() { std::cout << "Called public method of BaseClass" << std::endl; }
	BaseClass(int priv, int pub) : privateId(priv), publicId(pub) {}
protected:
	void protectedMethod() { std::cout << "Called protected method of BaseClass" << std::endl; }
};

class ChildClass1 : public BaseClass {
private:
	bool isChild;
public:
	ChildClass1(int priv, int pub) : BaseClass(priv, pub), isChild(true) {}
};

// Private inheritance: implements a 'has-a' relationship to the BaseClass
class ChildClass2 : private BaseClass {
private:
	bool isChild;
public:
	ChildClass2(int priv, int pub) : BaseClass(priv, pub), isChild(true) {}
	void callBaseClassPublicMethod() { publicMethod(); } // Inherits the publicMethod of the base class as a PRIVATE member
	void callBaseClassProtectedMethod() { protectedMethod(); } // Has access to protected members of base class, even though these are not accessible to world
};

int main(int argc, char const *argv[]) {
	MyClass m(23, "milo");

	SpreadOut s(100, "GOD");
	s.reciteBeeMovieScript("By all known laws of aviation...");

	// Test out constructors
	DefaultConstructorTest withoutArg;
	DefaultConstructorTest withArg("the sum of all natural numbers is -1/12!");


	// test out initializer list
	InitializerListTest ilt; // this should call default constructor on all members: "Called default constructor"
	InitializerListTest usingil(true); // "my default constructor was not called"

	OverloaderPlus op1;
	OverloaderPlus op2;
	op1 + op2; // "Using the overriden addition operator"

	TestThisKeyword me;
	me.isThisMe(me); // Expect you passed me into myself
	me.isThisMe(TestThisKeyword()); // Expect someone else

	//Test public/private inheritance
	BaseClass base(1, 2);
	ChildClass1 c1(3, 4);
	ChildClass2 c2(5, 6);

	std::cout << base.publicId << std::endl;
	base.publicMethod();

	c1.publicMethod();
	std::cout << c1.publicId << std::endl; // allowed to use all public members of base class as if they were in child class
	c2.callBaseClassPublicMethod(); // error: cannot access the private member of the base class from child
	// c2.publicMethod(); // not allowed because ChildClass2 inherits from private members of BaseClass ?
	c2.callBaseClassProtectedMethod();
	// base.protectedMethod(); // not allowed because this is protected!!!

	return 0;
}
