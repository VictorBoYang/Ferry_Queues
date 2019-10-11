from Circle_Queues import *


def move_car_into_queue(id_current, car_queue, car_line_list, list_current, car_left, car_added):
    car = Car(id_number=id_current)
    car_queue.push(car.id_number)
    car_line_list[list_current] = car_line_list[list_current] + 1
    id_current = id_current + 1
    car_left = car_left - 1
    car_added = car_added + 1
    return id_current, car_queue, car_line_list, list_current, car_left, car_added


def command_add(number_of_add_car, car_queue, car_add_id, list_add_count, car_line_list):
    id_current = car_add_id
    list_current = list_add_count
    car_left = number_of_add_car  # if all queues full, car_left can count how many cars left
    car_added = 0
    for i in range(number_of_add_car):
        if i == number_of_add_car - 1 and car_line_list[list_current] != car_queue.max:
            id_current, car_queue, car_line_list, list_current, car_left, car_added = move_car_into_queue(
                id_current,
                car_queue,
                car_line_list,
                list_current,
                car_left,
                car_added)
            print("added %d cars to lane %d" % (car_added, list_current+1))
            return id_current, list_current, car_line_list
        if car_line_list[list_current] == car_queue.max:  # decide if one line is full or not
            list_current = list_current + 1  # if full, move the new cars to next line
            print("added %d cars to lane %d" % (car_added, list_current))
            car_added = 0
            if list_current == 10:
                list_current = 0
                if car_line_list[list_current] == car_queue.max:  # decide if the next car queue also full
                    print("Could not add %d cars. All queues full." % car_left)  # if the next line also full, that
                    # means all queues full
                    return id_current, list_current, car_line_list
                else:
                    id_current, car_queue, car_line_list, list_current, car_left, car_added = move_car_into_queue(
                        id_current,
                        car_queue,
                        car_line_list,
                        list_current,
                        car_left,
                        car_added)
            else:
                id_current, car_queue, car_line_list, list_current, car_left, car_added = move_car_into_queue(
                    id_current,
                    car_queue,
                    car_line_list,
                    list_current,
                    car_left,
                    car_added)
        else:
            id_current, car_queue, car_line_list, list_current, car_left, car_added = move_car_into_queue(
                id_current,
                car_queue,
                car_line_list,
                list_current,
                car_left,
                car_added)
    return id_current, list_current, car_line_list


def check_user_input(user_input, car_queue, car_add_id, list_add_count,
                     car_line_list):
    if user_input == "add":
        car_add_amount = input("number of cars:")
        car_add_amount = int(car_add_amount)
        car_add_id, list_add_count, car_line_list = command_add(car_add_amount, car_queue, car_add_id, list_add_count,
                                                                car_line_list)
        return car_add_id, list_add_count, car_line_list
    elif user_input == "load":
        pass
    elif user_input == "exit":
        pass
    else:
        print("Invalid Command")
        return car_add_id, list_add_count, car_line_list