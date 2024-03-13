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
    
# The brute force way
def removeNthFromEndBF(head, n):
    """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
    """
    # Get length of linked list
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    # Index of the element to remove
    ind = length - n
  
    if length != 1:
        if ind == 0:
            head = head.next
        else:
            # Traverse the list until element and remove it
            curr = head
            for i in range(ind):
                if i == ind - 1:
                    curr.next = curr.next.next
                curr = curr.next   
    else:
        head = None
    
    return head


def reverseLinkedList(head):
    prev = None
    current = head 
    
    while current is not None: 
        next = current.next
        current.next = prev 
        prev = current 
        current = next
        
    head = prev
    
    return head

def removeNthFromEndReverse(head, n):
    """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
    """
    # Reverse the linked list
    head = reverseLinkedList(head)
    
    # Remove the nth node from the end
    prev = None
    curr = head
    for _ in range(n - 1):
        prev = curr
        curr = curr.next
    if prev:
        prev.next = curr.next
    else:
        head = head.next
    
    # Reverse the linked list again
    head = reverseLinkedList(head)
    
    return head
            
        

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
    
    node2 = ListNode(2)
    head4 = ListNode(1, node2)
    
    # Examples
    input = [
        (head1, 2, [1,2,3,5]),
        (head2, 1, []),
        (head3, 1, [1]),
        (head4, 2, [2])
    ]

    for idx, (head, n, expected) in enumerate(input):
        print("\nExample", idx, ":")
        print("Input:", linkedListString(head), n)
        print("Output:", linkedListString(removeNthFromEndReverse(head, n)))
        print("Expected:", expected)