'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def printLinkedList(head):
    current_node = head
    linked_list_str = '['
    while current_node:
        linked_list_str += str(current_node.val)
        if current_node.next:
            linked_list_str += ','
        current_node = current_node.next
    linked_list_str += ']'
    print(linked_list_str)
    
    
def removeNthFromEnd(head, n):
    """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
    """
    pass

# Some Test cases
if __name__ == "__main__":
    
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head1 = ListNode(1, node2)
    
    head2 = ListNode(1)
    
    node2 = ListNode(2)
    head3 = ListNode(1, node2)
    
    
    printLinkedList(head1)
    printLinkedList(head2)
    printLinkedList(head3)
    
    # # Invalid examples
    # input = [
    #     ("({})[", False),  
    #     ("[(])", False),   
    #     ("{[}", False),    
    #     ("{[()]}", True), 
    #     ("([{}))", False), 
    #     ("{[()]", False),  
    # ]

    # for idx, (head, n, expected) in enumerate(input):
    #     print("\nExample", idx, ":")
    #     print("Input:", head, n)
    #     print("Output:", removeNthFromEnd(head, n))
    #     print("Expected:", expected)