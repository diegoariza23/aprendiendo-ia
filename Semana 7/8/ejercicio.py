class Vehicle:
    color="white"
    
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        self.seating_capacity=None
    
    def seating(self,seating_capacity):
        self.seating_capacity=seating_capacity
    
    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

Toyota=Vehicle(200,50000)
Toyota.seating(5)
Toyota.display_properties()

Spark=Vehicle(180,75000)
Spark.seating(4)
Spark.display_properties()