/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) 
{
    struct ListNode *p,*q;
    struct ListNode t;
    t.next = head;
    p = &t;
    q = &t;
    for(int i =0; i<n+1 ; i++)
    {
        p = p->next;
    }
    while(p)
    {
        p = p->next;
        q = q->next;
    }
    struct ListNode *temp = q->next;
    q->next = temp -> next;
    return t.next;
}