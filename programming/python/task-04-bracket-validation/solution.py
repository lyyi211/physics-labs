#варіант 16 (6)

class Node:
    def __init__(self, cargo, next=None):
        self.cargo = cargo
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self, e):
        self.head = Node(e, self.head)

    def removeFirst(self):
        if self.head is None:
            raise SystemError
        value = self.head.cargo
        self.head = self.head.next
        return value

    def is_empty(self):
        return self.head is None

class Stack:
    def __init__(self):
        self.data = LinkedList()

    def push(self, e):
        self.data.addFirst(e)

    def pop(self):
        return self.data.removeFirst()

    def is_empty(self):
        return self.data.is_empty()

def check_brackets(a):
    stack = Stack()
    match = {')': '(', ']': '[', '}': '{'}

    for char in a:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != match[char]:
                return False

    return stack.is_empty()

a = input("Введіть рядок з дужками: ")
if check_brackets(a):
    print("Дужки розставлені правильно.")
else:
    print("Дужки розставлені неправильно.")
