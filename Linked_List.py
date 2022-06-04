"""
Input: N=2
LinkedList={1 , 2}
Output: 1 2
Explanation:
The linked list contains two 
elements 1 and 2.The elements 
are printed in a single line.
"""


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
        
def create_linked_list(list):

    """
       Create a linked list using a list object

       : param list : Linked_List object
            Stores all Node object created
    """
    # Get the number of nodes to be created
    number = int(input("Enter number of numbers: "))
    # Create a new node item i.e. the first node
    node  = Node(input("Enter data for node: "))
    # Set the new node item to the head 
    list.head = node
    
    # Check if number of nodes to be created is greater that 0
    while (number -1) > 0:

        # Create another node and set it as the next node
        node.next = Node(input("Enter data for node: "))
        # Set the newly created as the last node
        node = node.next
        # Decrease the number of nodes still to be created
        number -= 1
    
def print_linked_list(linked_list):

    """
       Print all the nodes in the list

       : param linked_list : Linked_List object
            List where all the nodes are stored
    """

    # Create a node to move through the list and set it to the head of the list
    traverse = linked_list.head
    
    # If there are other nodes after display the data in each Node
    while traverse != None:
        # Display current node data 
        print(traverse.data)
        # Set the next node 
        traverse = traverse.next

# Create a new Linked_list object
new_linked_list = Linked_list()
# Method calls 
create_linked_list(new_linked_list)
print_linked_list(new_linked_list)

# Given a singly linked list. The task is to find the length of the linked list, 
# where length is defined as the number of nodes in the linked list.
print("\nCheck number of nodes created")       
another_linked_list = Linked_list()
create_linked_list(another_linked_list)

def count_nodes(list):
        
    """
    Count the number of nodes in a list
    
        : param list : Linked_List object
            List where all the nodes are stored
    """

    # Initialize the counter variable
    counter = 0

    # Create a node to move through the list and set it to the head of the list
    traverse = list.head

    # Go through the list until the last node
    while traverse != None:
        # Get the next node
        traverse = traverse.next 
        # Increase the counter every time a node is changed
        counter += 1

    return counter


print_linked_list(another_linked_list)
print(f"Number of Nodes in Linked List: {count_nodes(another_linked_list)}")



# Implement the insertFirst method that inserts a new node with the given data key at the front of the linked list. 
# Assume the list is not empty.

def insert_first(list, node):

    """
    Insert new node as the head of the list
    
        : param list : Linked_List object
            List where all the nodes are stored
        : param node : Node
            The new node to add to the list
    """

    # Store the current head of the list as a temp value
    temp_head = list.head
    
    # If the current head is not empty
    if temp_head != None:
        # Set head as the new node
        list.head = node
        # Set the new node next node to the old head node
        node.next = temp_head
    else:
        # If list is empty set the head to new node
        list.head = node

print("\nHead Insertion")        
new_node = Node("158")
insert_first(another_linked_list,new_node )
print_linked_list(another_linked_list)

print("\nEmpty List Insertion")
new_node = Node("75")
next_linked_list = Linked_list()
insert_first(next_linked_list,new_node )
print_linked_list(next_linked_list)

# Implement the delete method that deletes a node with the given data key from the related LinkList object, and returns the Node containing the key. 
# Assume the list is not empty. If the key does not exist in the list, null should be returned and no action should be taken.

def delete_selected_node(list, key):
    """
    Delete the node that data is the same as the data entered
    
        : param list : Linked_List object
            List where all the nodes are stored
        : param key : int
            The data to look for
    """

    # Create a node to move through the list and set it to the head of the list
    traverse = list.head
    # Initialize the value of the node_found to 0
    node_found = None

    # Check if the data is found at head
    if traverse.data == key:
        # Set the head of the list to the next node
        list.head = traverse.next
    # If the data isn't at the head
    else:
        # Set the previous node to the head
        previous_node = list.head
        
        # Go through the list
        while traverse != None:

            # Check if the data entered matches the data at the current node
            if traverse.data == key:
               # Set the previous node next pointer to the current node next pointer
               previous_node.next = traverse.next
               # Set node_found to the actually node
               node_found = traverse
               break
           # If data is not in the current node
            else:
                # Set the previous node to the current node
                previous_node = traverse
                # Set the current node to the current node's next node
                traverse = traverse.next

    return node_found
     
print("\nSelected Deletion")
find_node = "89"
print(f"Deleted Node: {delete_selected_node(another_linked_list,find_node )}")
print_linked_list(another_linked_list) 

# Insert a new node, after a given node

def insert_node(list, key, new_node):
    """
    Insert node before a node with the given data.
    
        : param list : Linked_List object
            List where all the nodes are stored
        : param key : int
            The data to look for
        : param new_node: Node
            The node to be inserted
    """
     # Create a node to move through the list and set it to the head of the list
    traverse = list.head

    # Check if the list is empty
    if traverse == None:
        return None
    else:
        
        # Set the previous node to the head
        previous_node = list.head

        # Check if list is empty
        while traverse != None:
            
            # Check if the current node data is the data entered
            if traverse.data == key:
                # Set the previous node to the new node
                previous_node.next = new_node
                # Set the new node next node to the current node
                new_node.next = traverse
                break
            else:
                 # Set the previous node to the current node
                previous_node = traverse
                # Set the current node to the current node's next node
                traverse = traverse.next
                
print("\nSelected Insertion")
to_find = "78"
add_node = Node("185")
insert_node(another_linked_list,to_find,add_node)
print_linked_list(another_linked_list) 
