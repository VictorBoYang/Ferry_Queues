from Circle_Queues import *
from function_storage import *




def command_load():
    pass


def check_user_input(user_input):
    pass


def command_add(number_of_car, car_queue, car_id,list_count):
    id_current = car_id
    list_current = list_count
    for i in range(number_of_car):
        id_current = id_current + 1
        car = Car(id_number = id_current)
        car_queue.push(car.id_number)
        list_current = list_current + 1
    return id_current,list_current
        # car_queue.is_full()


car_line_list = [30] * 10  # Total ten lines for awaiting car, each line has a capacity of 30 cars.

car_queue = circle_queues(30)
car_id = 0
list_count = 0
car_id,list_count = command_add(15,car_queue,car_id, list_count)
print(list_count)
car_id,list_count = command_add(15,car_queue,car_id,list_count)
print(list_count)




# car_queue.push(car2)
# car_queue.push(car5)
# car_queue.peek()
# car_queue.pop()
# car_queue.pop()
# command_add(30,car_queue)
