class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Accelerate method
    def accelerate(self):
        self.__speed += 5

    # Brake method
    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    # Get speed method
    def get_speed(self):
        return self.__speed


# Program to create a Car object and test acceleration and braking
def main():
    # Create a Car object
    my_car = Car(2022, "Toyota")

    # Accelerate and display speed five times
    print("Accelerating:")
    for i in range(5):
        my_car.accelerate()
        print(f"Speed after acceleration {i+1}: {my_car.get_speed()}")

    # Brake and display speed five times
    print("\nBraking:")
    for i in range(5):
        my_car.brake()
        print(f"Speed after braking {i+1}: {my_car.get_speed()}")


# Run the program
if __name__ == "__main__":
    main()
