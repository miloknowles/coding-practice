/* Find the gcd(a, b) using Euclid's algorithm */
#include <stdio.h>
#include <iostream>

int gcd(int a, int b) {
	while (a > 0 && b > 0) {
		if (a > b) {
			a -= b;
		} else {
			b -= a;
		}
	}
	return (a > 0 ? a : b);
}

void printTest(int a, int b, int res) {
	std::cout << "gcd(" << a << ", " << b << ") = " << res << std::endl;
}

int main(int argc, char const *argv[])
{
	printTest(1, 1, gcd(1, 1));
	printTest(2, 1, gcd(2, 1));
	printTest(13, 39, gcd(13, 39));
	printTest(1000, 100, gcd(1000, 100));
	printTest(14, 21, gcd(14, 21));
	return 0;
}