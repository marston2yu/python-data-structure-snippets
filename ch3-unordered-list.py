# this file implement a unordered list.

# basic block of a unordered list is node.
class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    # simplest way to add a new data to a list is add in the front, otherwise we need to track the current pos.
    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False

    def size(self):
        current = self.head
        cnt = 0
        while current is not None:
            cnt = cnt + 1
            current = current.getNext()
        return cnt

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.getData() == item:  # if found, then set previous' next to current's next, which literally means
                # delete this node.
                if previous is None:  # delete the only node means set head to null.
                    self.head = None
                else:
                    previous.setNext(current.getNext())
                return True  # found.
            else:
                previous = current
                current = current.getNext()
        return False  # not found


if __name__ == '__main__':
    myList = UnorderedList()
    print(myList.isEmpty())
    myList.add(3)
    myList.add(4)
    print(myList.isEmpty())
    print(myList.search(18))
    print(myList.search(3))
    print(myList.size())

    print(myList.remove(18))
    print(myList.remove(3))
    print(myList.size())

    print(myList.remove(4))
    print(myList.isEmpty())
