/*
https://leetcode.com/problems/maximum-product-of-three-numbers/description/
Find the maximum product of 3 elements from an array.
*/
#include <iostream>
#include <algorithm>
#include <vector>

int maxTripleProduct(std::vector<int> nums) {
	std::sort(nums.begin(), nums.end());
	int negSum = nums[0] * nums[1] * nums[nums.size()-1]; // Use the 2 smallest and largest element (in case the 2 smallest are large negatives)
	int posSum = nums[nums.size()-1] * nums[nums.size()-2] * nums[nums.size()-3]; // Use the 3 highest numbers
	return std::max(negSum, posSum);
}

int main(int argc, char const *argv[])
{
	std::vector<int> v1 = {1,2,3,4}; // 24
	std::vector<int> v2 {-14, -15, 2, 6}; // 210 * 6 = 1260

	int res1 = maxTripleProduct(v1);
	int res2 = maxTripleProduct(v2);

	std::cout << res1 << std::endl;
	std::cout << res2 << std::endl;
	return 0;
}