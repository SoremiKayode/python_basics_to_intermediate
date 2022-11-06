# oop = objected oriennted programming

class Honda() :
    def __init__(self, brand, speed, year_of_manufacturing, engine_type):
        self.brand = brand
        self.speed_kmh = speed
        self.year_manufacturing = year_of_manufacturing
        year_of_manufacturing = 2008
        self.engine_type = engine_type

    def turn_left(self):
        print("Turn left")
    def run(self):
        print(f"I am running at {self.speed_kmh} kilometers per hour")

class Tesla(Honda):
    def __init__(self, brand, speed, year_of_manufacturing, engine_type, fly_level,):
        super().__init__(brand, speed, year_of_manufacturing, engine_type)
        self.fly_level = fly_level


vehicle = Tesla("Tesla", 250, 2009, "v8", "100")

vehicle.run()
vehicle.turn_left()


