#include <vector>
#include <unordered_map>
#include <stdio>

vector<int> findDuplicates(vector<int>& nums) {
		// Store number of times an element occurs.
    std::unordered_map<int, int> freqCtr;
    
    for (int i : nums) {
        if (freqCtr.find(i) != freqCtr.end()) {
            freqCtr[i]++;
        } else {
            freqCtr[i] = 1;
        }
    }
    std::vector<int> result;
    for (std::unordered_map<int,int>::iterator it = freqCtr.begin(); it != freqCtr.end(); ++it) {
        std::cout << it->first << std::endl;
        if (freqCtr[it->first] >= 2) {
            result.push_back(it->first);
        }
    }
    return result;
}