class Vehicles():
    def __init__(self,color,value):
        self.color = color
        self.max_speed = 50
        self.__value = value
    def get_value(self):
        return self.__value
    def set_value(self,new_value):
        self.__value = new_value
    def set_max_speed(self,newspeed):
        self.max_speed = newspeed

vehicle1 = Vehicles("red",200500)
vehicle1.set_value(40)
print(vehicle1.get_value())


class Car(Vehicles):
    def __init__(self,color,value,brand):
        super().__init__(color,value)
        self.brand = brand
    def show_details(self):
        print(self.color,self.max_speed,self.get_value(),self.brand)

car1 = Car("yellow",1000,"tesla")
car1.set_max_speed(100)
car1.show_details()