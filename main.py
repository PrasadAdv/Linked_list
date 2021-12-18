class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __int__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        if self.head is None:
            self.head = new_node
            return

    def insert(self, new_data, position):
        count = 1
        prev_node = self.head

        if prev_node is None:
            print("\n Previous node must exist to insert a new node after it.")
            return

        while count < (position-1):
            prev_node = prev_node.next
            count += 1

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def delete(self, position):
        count = 0
        prev_node = self.head

        if prev_node is None:
            print("\n Previous node must exist to delete a node after it.")
            return

        temp = 0
        if position > 0:
            while count < position:
                temp = prev_node
                prev_node = prev_node.next
                count += 1
            temp.next = prev_node.next
            temp = None

        else:
            self.head = prev_node.next
            prev_node = None


if __name__ == '__main__':
    llist = LinkedList()
    print('\n Enter nodes to create Linked list and press 'q' key on keyboard to stop input:\n')
    x = 0
    while x != 'q':
        x = input()
        if x != 'q':
            llist.push(x)

    print('\nLinked list is:', end=' ')
    llist.printlist()

    print('\nDo you want update the linked list? (Y/N):')
    res = input()

    if res is 'Y':
        while res is 'Y':
            print('\nWhat operation do you want perform?'
                  '\n1.Add node at the start.'
                  '\n2.Add node in between.'
                  '\n3.Add node at the end.'
                  '\n4.Delete a node.')
            choice = input()

            if choice == '1':
                print("\nEnter the nodes", end=' ')
                x = 0
                while x != 'q':
                    x = input()
                    if x != 'q':
                        llist.push(x)
                print("\nUpdated list is   :", end=' ')
                llist.printlist()

            elif choice == '2':
                print("\nEnter the node and position", end=' ')
                x = input()
                y = input()
                if x != 'q':
                    llist.insert(x, int(y))
                print("\nUpdated list is   :", end=' ')
                llist.printlist()

            elif choice == '3':
                print("\nEnter the nodes", end=' ')
                x = 0
                while x != 'q':
                    x = input()
                    if x != 'q':
                        llist.append(x)
                print("\nUpdated list is   :", end=' ')
                llist.printlist()

            elif choice == '4':
                print("\nEnter the position", end=' ')
                y = input()
                if y != 'q':
                    llist.delete(int(y))
                print("\nUpdated list is   :", end=' ')
                llist.printlist()
            print("\nDo you want to continue? (Y/N)\t", end=" ")
            res = input()

        print("\nNew list is   :", end=' ')
        llist.printlist()
    else:
        print("\nThank You!")
