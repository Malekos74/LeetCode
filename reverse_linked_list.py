# Definition for singly-linked list.
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

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        pass
    else:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next 
             
            curr.next = prev  
            prev = curr      
            
            curr = next_node 
            
        head = prev
        
    return head


# Some Test cases
if __name__ == "__main__":
    
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head1 = ListNode(1, node2)
    
    node2 = ListNode(2)
    head2 = ListNode(1, node2)
    
    head3 = None
    
    # Examples
    input = [
        (head1, [5,4,3,2,1]),
        (head2, [2,1]),
        (head3, [])
    ]

    for idx, (head, expected) in enumerate(input):
        print("\nExample", idx, ":")
        print("Input:", linkedListString(head))
        print("Output:", linkedListString(reverseList(head)))
        print("Expected:", expected)
    