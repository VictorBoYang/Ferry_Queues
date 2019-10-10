class Car:
    def __init__(self, id_number):
        self.id_number = id_number


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def output_data(temp_data):
    print("car'id: ", temp_data.id_number)


class Queues:
    def __init__(self):
        self.count = 0
        self.front = None
        self.back = None

    def push(self, new_data):
        temp = Node(data = new_data, next_node = None)
        if self.back is None:
            self.front = temp
        else:
            self.back.next_node = temp
        self.back = temp
        self.count = self.count + 1

    def pop(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp_data = self.front.data
            temp_node = self.front.next_node
            del self.front
            self.front = temp_node
            self.count = self.count - 1
            output_data(temp_data)

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            output_data(self.front.data)

