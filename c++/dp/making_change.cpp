/* Find the number of ways of making change for 'n' units using coins having the values given by 'c' */

#include <bits/stdc++.h>
#include <unordered_map>
#include <string>
#include <stdio.h> // make sure this is .h
#include <vector>

using namespace std;

void printCoins(vector<long> c) {
    for (long coin : c) {
        std::cout << " " << coin;
    }
    std::cout << std::endl;
}

// Store subproblem results
std::unordered_map<std::string, long> memo;

// Make the subproblems hashable
std::string stringify(long n, vector<long> c) {
    std::string res = std::to_string(n) + ".";
    for (long ci : c) {
        res += std::to_string(ci) + '.';
    }
    return res;
}

long getWays(long n, vector < long > c) {
    if (n == 0) { // Made successful change
        return 1;
    } else if (c.size() == 0 || n < 0) { // Ran out of coins or used coin bigger than n
        return 0;
    } else {
        if (memo.find(stringify(n, c)) != memo.end()) {
            return memo[stringify(n, c)];
        } else {
            long total = 0;
            
            // Case 1: use the first available coin
            if (c[0] <= n) {
                total += getWays(n-c[0], c);
            }
            
            // Case 2: skip the first coin
            vector<long> copy(++c.begin(), c.end());
            total += getWays(n, copy);
            
            std::string key = stringify(n, c);
            memo[key] = total;
            return total;
        }
    }
}

template <class T>
void printVect(std::vector<T> v) {
    for (T vi : v) {
        std::cout << vi << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    std::vector<long> c = {2, 5, 3, 6};
    long n = 10;

    long ways = getWays(n, c);

    std::cout << "Change for: " << n << std::endl;
    std::cout << "With coins: ";
    printVect<long>(c);
    std::cout << ways << std::endl;
    return 0;
}