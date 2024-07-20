class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    #inserting nodes

    # inserting at ending(appending)
    def append(self, data):
        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    # inserting at beggining
    def prepend(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    #inserting at any point
    def insert(self, data, position):
        new_node = Node(data=data)

        if position == 0:
            self.prepend(data=data)
            return
        
        prev_node = self.head
        for i in range(position - 1):
            if prev_node is None:
                return 'position out of bound'
            
            prev_node = prev_node.next
        
        new_node.next = prev_node.next
        prev_node.next = new_node
    

    def size(self):
        cur_node = self.head
        length = 0

        while cur_node is not None:
            cur_node = cur_node.next
            length+=1
        
        return length


    # Deleting nodes 
    # pop deleting last node

    def pop(self):
        size = self.size()

        if size == 0:
            return 'can\'t perform pop operation on an empty list'
        cur_node = self.head

        if size == 1:
            data = self.head.data   
            self.head = None
            return data
        
        for i in range(size - 2):
            cur_node = cur_node.next
        
        last_node_data = cur_node.next.data
        cur_node.next = None
        return last_node_data
    
    def delete_at(self, position):
        if self.head is None:
            return 'Linked list is empty'
        
        if position == 1:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(position-1):
            if current.next is None:
                raise IndexError('position out of bounds')
            current = current.next
            
        if current.next is None:
            raise IndexError('position out of bounds')
        current.next = current.next.next    
        

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def print_list(self):
        current = self.head
        result = ['head']

        while current is not None:
            result.append(str(current.data))
            current = current.next
        result.append('None')
        return '->'.join(result)



ll = LinkedList()

ll.append(20)
ll.prepend(10)
ll.append(100)
ll.append(200)
ll.append(300)

print(ll.print_list())
ll.reverse()
print(ll.print_list())