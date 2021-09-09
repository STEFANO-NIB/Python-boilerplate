from src.car.car_repo import CarRepo


class CarService():
    def __init__(self):
        self.color = ''
        self.is_dirty = False
        self.hours_spent = 0
        self.license_plate = ''
        #Using the car repo's functionality
        self.car = CarRepo()


    # Private function that is only to be used in the CarService. 
    # This calculates the car parking price based on it's variables
    def _calc_parking_price(self, color, is_dirty, hours_spent):
        #List of colors that would have a discount
        color_list = ['red', 'blue', 'black']
        #The fixed hourly rate for parking
        rate = 7 
        hours = hours_spent or 0
        #Trim and lowercase user inputted colors for accurate comparisons
        new_color = str(color).strip().lower()

        if (new_color in color_list):
            if (is_dirty):
                return (rate * .5) * hours
            else:
                return (rate * 0) * hours

        if (new_color not in color_list):
            if (is_dirty):
                return (rate * 2) * hours
            else:
                return rate * hours

    def get_cars(self):
        carList = self.car.find_all_cars()
        if (not carList):
            return {"error: 'No cars were found'"}

        return carList

    def get_car(self, license_plate):
        car = self.car.find_car(license_plate)
        if (not car):
            return {"error": 'No cars were found'}
        return car

    def create_car(self, color, is_dirty, hours_spent, license_plate):
        price = self._calc_parking_price(
            color=color,
            is_dirty=is_dirty,
            hours_spent=hours_spent)

        try:
            # Would recommend validation that prevents users from creating a car with no values
            return self.car.add_car(
                color=color,
                is_dirty=is_dirty,
                hours_spent=hours_spent,
                license_plate=license_plate,
                price=price)
        except ValueError as e:
            return {
                "error": 'A car with that license plate is already parked in our garage'}

    def update_car(self, color, is_dirty, hours_spent, license_plate):
        # Test to see if car exists currently in the garage
        curr_car = self.get_car(license_plate)
        if (curr_car):
            # This checks to see if current data is being updated with new values.
            # If not, remain the same
            new_color = color or curr_car['color']
            new_is_dirty = is_dirty or curr_car['is_dirty']
            new_hours_spent = hours_spent or curr_car['hours_spent']

            # Created a updated version of the car to pass to the function
            updated_car = {
                "color": new_color,
                "is_dirty": new_is_dirty,
                "hours_spent": new_hours_spent,
                # Update the price based on new values passed
                "price": self._calc_parking_price(color=new_color, is_dirty=new_is_dirty, hours_spent=new_hours_spent)
            }

            return self.car.update_car(updated_car, license_plate=license_plate)
        else:
            f'There is no car of license plate {license_plate} currently parked in this garage'
    
    def delete_car(self, license_plate):
        curr_car = self.get_car(license_plate)
        if (curr_car):
            return self.car.remove_car(license_plate)
        
        return curr_car