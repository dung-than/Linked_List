
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    # Convert a linked list back into a Python list
    def to_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        return out_list


# Test cases
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

new_node = linked_list.head
while new_node:
    print(new_node.value)
    new_node = new_node.next

print("Pass" if linked_list.to_list() == [1, 2, 4] else "Fail")
