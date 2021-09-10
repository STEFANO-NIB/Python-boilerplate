from src import app
from flask import Flask, request, jsonify, request
from src.car.car_service import CarService

#Get all cars
@app.route('/cars', methods=['GET'])
def get_cars():
    carList = CarService().get_cars()
    return jsonify(carList), 200

#Get one car by license plate
@app.route('/car/<license_plate>', methods=['GET'])
def get_car(license_plate):
    car = CarService().get_car(license_plate)
    return jsonify(car), 200

#Add car to garage
@app.route('/car', methods=['POST'])
def add_car():
    data = request.get_json()
    car = CarService().create_car(
        color=data.get('color'),
        is_dirty=data.get('is_dirty'),
        hours_spent=data.get('hours_spent'),
        license_plate=data.get("license_plate")
    )

    return jsonify(car), 200

#Update existing car
@app.route('/car/<license_plate>', methods=['PUT'])
def update_car(license_plate):
    data = request.get_json()
    car = CarService().update_car(
        color=data["color"],
        is_dirty=data["is_dirty"],
        hours_spent=data["hours_spent"],
        license_plate=license_plate)

    return jsonify(car), 200

#Delete existing car
@app.route('/car/<license_plate>', methods=['DELETE'])
def delete_car(license_plate):
    car = CarService().delete_car(license_plate)
    return jsonify(car), 200
