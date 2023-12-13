
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles."


def main():
    car1 = Car("blue", 20_000)
    car2 = Car("red", 30_000)

    print(car1)
    print(car2)


if __name__ == "__main__":
    main()
