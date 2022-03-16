#Basado en el codigo de Debidutta Rath de internet
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


# Create & Handle List operations
class LinkedList:
	def __init__(self):
		self.head = None

	# Method to add element to list
	def addToList(self, newData):
		newNode = Node(newData)
		if self.head is None:
			self.head = newNode
			return

		last = self.head
		while last.next:
			last = last.next

		last.next = newNode


# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def merge(head1: Node, head2: Node):
	nodeAux = Node(0)
	ultimo = nodeAux
	while True:
		if head1 is None:
			ultimo.next = head2
			break
		if head2 is None:
			ultimo.next = head1
			break

		if head1.val <= head2.val:
			ultimo.next = head1
			head1 = head1.next
		else:
			ultimo.next = head2
			head2 = head2.next
		ultimo = ultimo.next
	return nodeAux.next


listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)

# Call the merge function
listA.head = merge(listA.head, listB.head)

