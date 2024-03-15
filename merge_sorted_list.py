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
        
def linkedListString(head):
    current_node = head
    
    linked_list_str = '['
    while current_node:
        linked_list_str += str(current_node.val)
        if current_node.next:
            linked_list_str += ', '
        current_node = current_node.next
    linked_list_str += ']'
    
    return linked_list_str
    
def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    return list1


# Some Test cases
if __name__ == "__main__":
    
    node3 = ListNode(4)
    node2 = ListNode(2, node3)
    head1 = ListNode(1, node2)
    
    node3 = ListNode(4)
    node2 = ListNode(3, node3)
    head2 = ListNode(1, node2)
    
    head3 = head4 = None
    
    head5 = None
    head6 = ListNode(0)
    
    # Examples
    input = [
        (head1, head2, [1,1,2,3,4,4]),
        (head3, head4, []),
        (head5, head6, [0])
    ]

    for idx, (head1, head2, expected) in enumerate(input):
        print("\nExample", idx, ":")
        print("Input:", linkedListString(head1), linkedListString(head2))
        print("Output:", linkedListString(mergeTwoLists(head1, head2)))
        print("Expected:", expected)