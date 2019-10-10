from demo.Queues import *

car1 = Car("122")
car2 = Car("123")
car3 = Car("124")
car4 = Car("125")
car5 = Car("126")

car_queue = Queues()
car_queue.push(car2)
car_queue.push(car5)
car_queue.peek()
car_queue.pop()
car_queue.pop()
