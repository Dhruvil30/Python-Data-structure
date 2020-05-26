class node:

	def __init__(self,data):
		self.data = data
		self.next = None

class link_list_operation:

	def __init__(self):
		self.head = None

	def insert_at_end(self,data):

		n = node(data)

		if self.head is None:
			self.head = n
		else:
			point = self.head
			while point.next: 
				point = point.next
			point.next = node(data)

	def insert_at_front(self,data):

		n = node(data)

		if self.head is None:
			self.head = n
		else:
			point = self.head
			self.head = n
			n.next = point

	def delete_at_last(self):

		if self.head is None:
			print("List is empty")
		else:
			point = self.head
			while point.next.next:
				point = point.next
			point.next = None

	def delete_at_front(self):

		if self.head is None:
			print("List is empty")
		else:
			self.head = self.head.next

	def print_list(self):

		if self.head is None:
			print("No elements in the list")
		else:
			point = self.head
			while point:
				print(point.data)
				point = point.next

root = link_list_operation()

root.insert_at_end(10)
root.insert_at_front(20)
root.insert_at_end(30)
root.insert_at_front(40)
root.delete_at_last()
root.delete_at_front()

root.print_list()


