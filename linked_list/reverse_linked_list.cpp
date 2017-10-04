#include <iostream>
#include <vector>

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

ListNode* reverseLinkedList(ListNode *head) {
	ListNode *prev = NULL;

	while (head) {
		ListNode *next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return prev;
}

ListNode* buildLinkedList(std::vector<int> v) {
	ListNode *head = new ListNode(v[0]);

	ListNode *current = head;
	for (int i : v) {
		current->next = new ListNode(i);
		current = current->next;
	}
	return head;
}

void printLinkedList(ListNode *head) {
	std::cout << "Linked list:" << std::endl;
	while (head) {
		std::cout << " " << head->val << " ";
		head = head->next;
	}
	std::cout << std::endl;
}

int main(int argc, char const *argv[])
{
	// Example
	// g++ reverse_linked_list.cpp -std=c++11
	std::vector<int> vect = {1, 2, 3, 4, 5, 6, 7, 8};
	ListNode *head = buildLinkedList(vect);
	printLinkedList(head);

	ListNode *revHead = reverseLinkedList(head);
	printLinkedList(revHead);
	return 0;
}