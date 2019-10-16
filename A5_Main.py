from function_storage import *


car_line_list = [circle_queues(30) for i in range(10)]
car_id = 1
list_index_count = 0
car_added_count = 0
list_load_count = 0
user_input = ""
while user_input is not None:
    user_input = input("Command: ")
    car_id, car_line_list, list_index_count, car_added_count, list_load_count = check_user_input(user_input, car_id, list_index_count,car_line_list, car_added_count, list_load_count)
    if user_input == "exit":
        user_input = None
        print("Exited")