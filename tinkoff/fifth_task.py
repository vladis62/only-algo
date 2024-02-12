def fifth_task(sequence):
    current_location = 1
    cars_in_points = {i: set() for i in range(1, len(sequence) + 2)}

    for car_number in sequence:
        # Проверяем, находится ли автомобиль в текущем пункте доставки
        if car_number in cars_in_points[current_location]:
            cars_in_points[current_location].remove(car_number)
        else:
            # Если автомобиль не в текущем пункте, то ищем его в следующих пунктах
            found = False
            for point in range(current_location + 1, len(cars_in_points) + 1):
                if car_number in cars_in_points[point]:
                    cars_in_points[point].remove(car_number)
                    current_location = point
                    found = True
                    break

            # Если автомобиль не найден в следующих пунктах, то посылка не доставится
            if not found:
                return False

    # Если все номера автомобилей из последовательности пройдены, посылка доставится
    return True
