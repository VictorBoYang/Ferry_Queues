from Circle_Queues import *
from function_storage import *


def command_load():
    pass


def check_user_input(user_input):
    pass


def move_car_into_queue(id_current, car_queue, car_line_list, list_current, car_left):
    car = Car(id_number=id_current)
    car_queue.push(car.id_number)
    car_line_list[list_current] = car_line_list[list_current] + 1
    id_current = id_current + 1
    car_left = car_left - 1
    return id_current, car_queue, car_line_list, list_current, car_left


def command_add(number_of_car, car_queue, car_id, list_count, car_line_list):
    id_current = car_id
    list_current = list_count
    car_left = number_of_car  # if all queues full, car_left can count how many cars left
    for i in range(number_of_car):
        if car_line_list[list_current] == car_queue.max:  # decide if one line is full or not
            list_current = list_current + 1  # if full, move the new cars to next line
            if list_current == 10:
                list_current = 0
                if car_line_list[list_current] == car_queue.max:  # decide if the next car queue also full
                    print("Could not add %d cars. All queues full." % car_left)  # if the next line also full, that
                    # means all queues full
                    return id_current, list_current, car_line_list
                else:
                    move_car_into_queue(id_current, car_queue, car_line_list, list_current, car_left)
                    # car = Car(id_number=id_current)
                    # car_queue.push(car.id_number)
                    # car_line_list[list_current] = car_line_list[list_current] + 1
                    # id_current = id_current + 1
                    # car_left = car_left - 1
            else:
                move_car_into_queue(id_current, car_queue, car_line_list, list_current, car_left)
        else:
            move_car_into_queue(id_current, car_queue, car_line_list, list_current, car_left)
    return id_current, list_current, car_line_list


car_line_list = [0] * 10  # Total ten lines for awaiting car, each line has a capacity of 30 cars.

car_queue = circle_queues(30)
car_id = 1
list_count = 0
car_id, list_count, car_line_list = command_add(400, car_queue, car_id, list_count, car_line_list)
print(list_count)

# car_queue.push(car2)
# car_queue.push(car5)
# car_queue.peek()
# car_queue.pop()
# car_queue.pop()
# command_add(30,car_queue)
