# Temp DB
car_list = []


class CarRepo:
    def __init__(self):
        self.car_list = []

    def find_all_cars(self):
        print(car_list)
        return car_list

    def find_car(self, license_plate):
        for c in car_list:
            if c['license_plate'] == license_plate:
                return c
        return ''

    def add_car(self, color, license_plate, is_dirty, hours_spent, price):
        for i in car_list:
            if i['license_plate'] == license_plate:
                raise ValueError(
                    'A car with that license plate is already parked in our garage')

        car_list.append({
            "license_plate": license_plate,
            "color": color,
            "is_dirty": is_dirty,
            "hours_spent": hours_spent,
            "price": price
        }) 
        return car_list[-1]

    def update_car(*args, license_plate):
        for car in car_list:
            if car["license_plate"] == license_plate:
                car['color'] = args[1]['color']
                car['hours_spent'] = args[1]['hours_spent']
                car['is_dirty'] = args[1]['is_dirty']
                car['price'] = args[1]['price']
                return car
        return {'error': 'No cars to update'}

    def remove_car(self, license_plate):
        for i, car in enumerate(car_list):
            if car["license_plate"] == license_plate:
                return car_list.pop(i)
        return {'error': 'No cars to delete'}  