# Queue Implementation maintaining head or start pointer at rear end
# With Singly Linked List we cannot perform pop operation as we do not have the address of previous node
# To solve this problem we may use Doubly linked List
# Operations are :
# 1. pop operation
# 2. push operation
# 3. peek operation
# 4. showList
class StackLinkedList:
    head = None

    class Node:
        data = None
        left = None
        right = None

    def push(self, value):
        node = self.Node()
        node.data = value
        node.left = None
        node.right = None
        if (self.head == None):
            self.head = node
        else:
            self.head.right = node
            node.left=self.head
            self.head=node

    def pop(self):
        if (self.head == None):
            print("List empty!")
        else:
            self.head=self.head.left
            self.head.right=None

    def peek(self):
        if self.head == None:
            print("No element in stack")
        else:
            print(self.head.data)

    def showList(self):
        if (self.head == None):
            print("List is empty")
        else:
            temp = self.head
            while (temp.left != None):
                temp = temp.left
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.right


    # This function helps in execution of the other functions (that perform various Linkedlist operations)
    def perform(self):
        print("1- PUSH")
        print("2- POP")
        print("3- PEEP")
        print("4- SHOW LIST")
        print("5- EXIT")
        continue_operation = 1
        while (continue_operation):
            ch = int(input("Enter the choice of operation : "))
            if ch == 1:
                val = int(input("Enter the element to insert : "))
                self.push(val)
            elif ch == 2:
                self.pop()
            elif ch == 3:
                self.peek()
            elif ch == 4:
                print("The list is : ", end="")
                self.showList()
                print()
            elif ch == 5:
                print("Quiting as per your wish !")
                exit()
            else:
                print("Wrong choice of operation")
            continue_operation=int(input("Do you want to continue ? (0--> No and 1-->Yes) : "))


# we are creating a linkedlist object
s = StackLinkedList()
s.perform()