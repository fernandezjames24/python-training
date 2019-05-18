# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


#instantiate Vehicle() object on two variables named car1 and car2

car1 = Vehicle()
car2 = Vehicle()


#assign values on variable members of Vehicle() class

#for car1
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00


#for car2
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00



# test code
print(car1.description())
print(car2.description())
