from Circle_Queues import *


def move_car_into_queue(car_left, car_line_list, car_added_count, list_index_count, car_id):
    car_id_count = Car(car_id)
    car_line_list[list_index_count].push(car_id_count)
    car_id = car_id + 1
    car_added_count = car_added_count + 1
    car_left = car_left - 1
    return car_left, car_line_list, car_added_count, list_index_count, car_id


def command_add(number_of_add_car, car_line_list, car_id, list_index_count, car_added_count):
    n = number_of_add_car
    car_left = n
    car_line_list = car_line_list
    car_id = car_id
    list_index_count = list_index_count
    for i in range(number_of_add_car):
        if i == n - 1 and car_line_list[list_index_count] != car_line_list[list_index_count].max:
            car_left, car_line_list, car_added_count, list_index_count, car_id = move_car_into_queue(car_left,
                                                                                                     car_line_list,
                                                                                                     car_added_count,
                                                                                                     list_index_count,
                                                                                                     car_id)
            print("added %d cars to lane %d" % (car_added_count, list_index_count + 1))
            car_added_count = 0
            return car_line_list, car_id, list_index_count, car_added_count
        if car_line_list[list_index_count].count == car_line_list[list_index_count].max:
            if car_added_count != 0:
                print("Added %d cars to Lane %d" % (car_added_count, list_index_count + 1))
            list_index_count = list_index_count + 1
            car_added_count = 0
            if list_index_count == 10:
                list_index_count = 0
            elif car_line_list[list_index_count].count == car_line_list[list_index_count].max:
                print("Could not add %d cars. All queues full." % car_left)
                return car_line_list, car_id, list_index_count, car_added_count
            else:
                car_left, car_line_list, car_added_count, list_index_count, car_id = move_car_into_queue(car_left,
                                                                                                             car_line_list,
                                                                                                             car_added_count,
                                                                                                             list_index_count,
                                                                                                             car_id)
        else:
            car_left, car_line_list, car_added_count, list_index_count, car_id = move_car_into_queue(car_left,
                                                                                                         car_line_list,
                                                                                                         car_added_count,
                                                                                                         list_index_count,
                                                                                                         car_id)
    else:
        car_left, car_line_list, car_added_count, list_index_count, car_id = move_car_into_queue(car_left,
                                                                                                     car_line_list,
                                                                                                     car_added_count,
                                                                                                     list_index_count,
                                                                                                     car_id)
    return car_line_list, car_id, list_index_count, car_added_count


def check_user_input(user_input, car_id, list_index_count, car_line_list, car_added_count):
    if user_input == "add":
        car_add_amount = input("number of cars:")
        number_of_add_car = int(car_add_amount)
        car_line_list, car_id, list_index_count,car_added_count = command_add(number_of_add_car, car_line_list, car_id,
                                                              list_index_count, car_added_count)
        return car_id, car_line_list, list_index_count, car_added_count
    elif user_input == "load":
        pass
    elif user_input == "exit":
        pass
    else:
        print("Invalid Command")
        return car_id, car_line_list, list_index_count, car_added_count
