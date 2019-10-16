class Car:
    def __init__(self, id_number):
        self.id_number = id_number


# def output_data(temp_data):
#     return temp_data.id_number


class circle_queues:
    def __init__(self, size_in):
        self.max = size_in
        self.a = [""] * self.max
        self.front = -1
        self.back = -1
        self.count = 0

    def push(self, new_data):
        if self.count == self.max:
            print("Queue is full")
        elif self.front == -1:
            self.front = 0
            self.back = 0
        elif self.back == self.max - 1:
            self.back = 0
        else:
            self.back = self.back + 1
        self.a[self.back] = new_data
        self.count = self.count + 1
        # print("pushed, the car's id is: ", self.a[self.back].id_number)

    def pop(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            temp = self.a[self.front]
            if self.front == self.back:
                self.front = -1
                self.back = -1
            elif self.front == self.max - 1:
                self.front = 0
            else:
                self.front = self.front + 1
            self.count = self.count - 1
            # print("removed, car'id is: ", self.a[self.front].id_number)

    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("The first car'id is: ", self.a[self.front])

    def is_full(self):
        if self.count == self.max:
            print("queue is full")

