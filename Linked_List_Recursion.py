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
        
def print_linked_list_recurisvely(node):

    """
       Print all the nodes in the list

       : param linked_list : Linked_List object
            List where all the nodes are stored
    """
    if node == None:
       print("End!")
    else:
        print(f"Node : {node.data}")  
        node = node.next
        print_linked_list_recurisvely(node)

# Create a linked list based on data from a database 

# Set global variables used by the different functions
names = ["Amy", "Dana", "Brent", "John", "Kerry", "Abby", "Kanika"]
START = 0
END = 1

def get_values():
    """

    """
    global START
    global END
    
    value = names[START:END]
    value = value[0]
    START += 1
    END += 1
    
    return value

def create_link_list_recursively(llist, value):
    
    # Create a new node everytime the method is called
    node = Node(value)
       
    # Check if it is the last person in the list
    if value == names[(len(names)-1)]:
        # If the last person set return the node
        return node
    else: 
        if llist.head == None:
             llist.head = node
             node.next = create_link_list_recursively(llist, get_values())
             return node
        else:
             node.next = create_link_list_recursively(llist, get_values())
             return node
            

print("\nCreate a Linked List using Recursion with predefine values")
new_linked_list = Linked_list()
create_link_list_recursively(new_linked_list, get_values())
print_linked_list_recurisvely(new_linked_list.head) 