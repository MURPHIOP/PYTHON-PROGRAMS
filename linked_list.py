class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

print("Creating Linked List...")

n = int(input("Enter number of nodes: "))
head = None
temp = None

for i in range(n):
    val = input(f"Enter data for node {i+1}: ")
    new_node = Node(val)
    if head is None:
        head = new_node
        temp = head
    else:
        temp.next = new_node
        temp = new_node

print("\nLinked List Created.")

# Display the linked list
print("\nDisplaying Linked List:")
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
