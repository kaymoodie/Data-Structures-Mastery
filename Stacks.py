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

        self.stack.pop(0)

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

string_exp1 = "{}()[]"
stack_1 = Stack()
if stack_1.empty():
    index = len(string_exp1) - 1
    while index >= 0:
        stack_1.push(string_exp1[index])
        index -=1

print(stack_1.stack)

