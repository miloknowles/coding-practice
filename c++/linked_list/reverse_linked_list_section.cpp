#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* reverseBetween(ListNode* head, int m, int n) {
    if (n == m) { return head; }

    // now guaranteed list has >= 2 elements, and n > m
    n = n-m;
    
    ListNode *start = new ListNode(0);
    start->next = head;
    
    ListNode *curr = start;

    // advance until reverse section begins
    while (--m) {
        curr = curr->next;
    }

    // curr is at the element BEFORE m
    ListNode *cutL = curr;
    curr = curr->next;
    ListNode *cutR = curr;
    
    ListNode *prev = curr;
    curr = curr->next;
    while (n--) {
        ListNode *tmp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = tmp;
    }

    // splice together new list
    cutR->next = curr;
    cutL->next = prev;
    return start->next;
}

ListNode* buildLinkedList(std::vector<int> v) {
    ListNode *head = new ListNode(v[0]);
    ListNode *curr = head;
    for (int i : v) {
        curr->next = new ListNode(i);
        curr = curr->next;
    }
    return head->next;
}

void printLinkedList(ListNode *head) {
    std::cout << "Linked list:" << std::endl;
    while (head) {
        std::cout << " " << head->val << " ";
        head = head->next;
    }
    std::cout << std::endl;
}

int main(int argc, char const *argv[]) {
    std::vector<int> v1 = {1,2,3,4,5,6,7};

    // reverse small section
    ListNode *ll1 = buildLinkedList(v1);
    printLinkedList(ll1);
    ListNode *rev1 = reverseBetween(ll1, 3, 5);
    printLinkedList(rev1);

    // reverse whole list
    ListNode *ll2 = buildLinkedList(v1);
    printLinkedList(ll2);
    ListNode *rev2 = reverseBetween(ll2, 1, 7);
    printLinkedList(rev2);

    return 0;
}