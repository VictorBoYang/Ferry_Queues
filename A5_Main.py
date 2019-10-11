from function_storage import *


def command_load(car_queue, list_load_count, car_line_list):
    # id_load_current = car_load_id
    list_current = list_load_count
    car_left = 100
    for i in range(100):
        if car_line_list[list_current] == 0:
            print("All queues empty.")
            return car_queue, list_load_count, car_line_list
        else:
            car_queue.pop()
            car_left = car_left - 1
            if car_line_list[list_current] == 0:
                list_current = list_current + 1
    return car_queue, list_load_count, car_line_list


car_line_list = [0] * 10  # Total ten lines for awaiting car, each line has a capacity of 30 cars.

car_queue = circle_queues(30)
car_add_id = 1
list_add_count = 0
list_load_count = 0
# car_add_id, list_add_count, car_line_list = command_add(160, car_queue, car_add_id, list_add_count, car_line_list)
# car_add_id, list_add_count, car_line_list = command_add(100, car_queue, car_add_id, list_add_count, car_line_list)
# car_add_id, list_add_count, car_line_list = command_add(30, car_queue, car_add_id, list_add_count, car_line_list)
user_input = ""
while user_input is not None:
    user_input = input("Command: ")
    car_add_id, list_add_count, car_line_list = check_user_input(user_input, car_queue, car_add_id, list_add_count,
                     car_line_list)
    if user_input == "exit":
        user_input = None
        print("Exited")
