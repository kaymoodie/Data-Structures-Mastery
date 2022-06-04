class Stack:

    def __init__(self):

        self.stack = []

    def empty(self):

        return len(self.stack) == 0

    def size(self):

        return len(self.stack)

    def top(self):

        return self.stack[0]

    def push(self,data):

        self.stack.insert(0, data)

    def pop(self):

       return self.stack.pop(0)

# Create a Stack object
new_stack = Stack() 
# Check if Stack object is empty then add items
print("Add to Stack")
if new_stack.empty():
    new_stack.push(123)
print(new_stack.stack)
new_stack.push(456)
print(new_stack.stack)
new_stack.push(789)
print(new_stack.stack)
new_stack.push(369)
print(new_stack.stack)
new_stack.push(258)
print(new_stack.stack)
new_stack.push(147)
print(new_stack.stack)

# Remove first item
print("\nRemove from Stack")
print(f"Current Stack: {new_stack.stack}")
new_stack.pop()
print(f"New stack: {new_stack.stack}")

# See first item
print("\nPeek Stack")
print(f"Top of Stack: {new_stack.top()}")

# Size of Stack
print("\nStack Size")
print(f"{new_stack.size()}\n")
   
# Given an expression string exp, write a program to examine whether the pairs and 
# the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.

def create_a_stack(data):

    stack = Stack()
    if stack.empty():
        index = len(data) - 1
        while index >= 0:
            stack.push(data[index])
            index -=1
    
    return stack

def check_balance(stack):

    pairs_dictionary = {"{":"}","[":"]", "(":")", }
    length = stack.size()
    balance = 0
  
    if length % 2 > 0:
        print("Not Balance!")
    else:
        pairs = int(length / 2)

        while stack.empty() != True:

            item1 = stack.pop()
            item2 = stack.pop()

            if pairs_dictionary.get(item1):
                side = pairs_dictionary[item1]
            else:
                side = ""

            if item2 == side:
                balance +=1

                       
        if balance == pairs:
        
            print("This arrangement is valid\n")
        else: 
            print("Arrangement not valid\n")

print("\nExercise 1")
string_exp = "{}()[]"
another_stack = create_a_stack(string_exp)
print(string_exp)
check_balance(another_stack)

string_exp = "[(])"
another_stack = create_a_stack(string_exp)
print(string_exp)
check_balance(another_stack)

string_exp = "([]"
another_stack = create_a_stack(string_exp)
print(string_exp)
check_balance(another_stack)


# Write an algorithm that will move the top value on one stack to the top of another stack
print("\nExercise 2")
stack_1 = create_a_stack([25,45,56,58,79,10])
print(f"Original Stack 1: {stack_1.stack}")
top_item = stack_1.pop()
stack_2 = create_a_stack([12,4,78,98])
print(f"Original Stack 2: {stack_2.stack}")
stack_2.push(top_item)
print(f"New Stack 1: {stack_1.stack}")
print(f"New Stack 2: {stack_2.stack}")


# Write an algorithm that starts with a stack containing
# n integers and finishes with the same integers in the same stack, but with the value that was
# on the bottom of the stack moved to the top, and all other values moved down one position.

print("\nExercise 3")
stack_2 = create_a_stack([4, 17, 9, 23])
print(f"Original Stack: {stack_2.stack}")
temp_stack = Stack()
top = stack_2.pop()

while stack_2.size() > 1:
    temp_stack.push(stack_2.pop())
else: 
    last_item = stack_2.pop()

while temp_stack.empty() != True:
    stack_2.push(temp_stack.pop())

stack_2.push(top)
stack_2.push(last_item)
print(f"New Stack Order: {stack_2.stack}")


print("\nAnother Exercise")
# Given a permutation of number from 1 to N. Among all the subarrays, find the number of unique pairs (a, b) such that a is not equal to b
# and a is maximum and b is second maximum in that subarray.

n = int(input("Enter input: "))

number_list = [num for num in range(1, n+1)]

list_of_subarray =[]

length = len(number_list)

for index in range(length):
    for next_index in range(index+1, length+1):
        list_of_subarray.append(number_list[index:next_index])

stack_of_subarray = create_a_stack(list_of_subarray)
stack_of_twos = create_a_stack([])
final_list = []

while stack_of_subarray.size() > 0:
    item = stack_of_subarray.pop()
    if len(item)==2:
        stack_of_twos.push(item)
print(stack_of_twos.stack)

while stack_of_twos.size() > 0:
    item = stack_of_twos.pop()
    final_list.append((item[1],item[0]))

for item in final_list:
    print(item)
        
        











