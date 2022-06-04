class Node:
    """
        A class used to represent a Node from a linked list
    """
    
    def __init__(self, data):

        """
            Initialize the Node class. 

            data : str
                The value store in the Node
            next: Node
                The location to the consecutive Node 
        """

        self.data = data
        self.next = None
        
class Linked_list:
    """
        A class that is use to represent a list of Node items
    """
    def __init__(self):
        """
            Initialize the Linked List class

            head : Node
                Initialize the head of the list
        """
        self.head = None
  
   
    def add(self, item):
        # Create a new node to add to list
        node = Node(item)
        # Set the node to traverse the list
        traverse_node = self.head

        # Check if this is first node item to be added on the list
        if self.head == None:
            # Set it to head
           self.head = node
           # Set the next point to the head
           self.head.next = self.head
        # If there are items in the list
        else:
            # Check if there other items in the list
            while True:   
                # Check if the next node is head             
                if traverse_node.next == self.head:
                    # If true
                    # Set the next node to the new node
                    traverse_node.next = node
                    # The set the next pointer to head 
                    node.next = self.head
                    # End the loop when the list is back at the top
                    break
                # Get the next node in the list if the current node next doesn't point to head
                traverse_node = traverse_node.next
            
    def print(self):
        
        # Get the first item on the list
        current_node = self.head
        
        # Check if list is empty
        if self.head is not None:
            
            while(True):
                # Print each node data in the list
                print(f"Node { current_node.data}", end="\n")
                # Get the next node
                current_node =  current_node.next
                # Check if it is at the top of the list
                if current_node == self.head:
                    print("Back at head!")
                    break
                
clinkedlist = Linked_list()
for item in range(1,10):
    clinkedlist.add(item)

clinkedlist.print()
      
            
            
        