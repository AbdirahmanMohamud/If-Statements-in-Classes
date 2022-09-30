#define the class of Car Guide
class carguide:
    #define attributes for the class
    name = ""
    kind = ""
    colour = ""
    value = ""
    #creates a statement for the attributes to use
    def description(self):
        desc_str = "%s is a %s %s that costs £%s" % (self.name, self.colour, self.kind, self.value)
        return desc_str
#adds attributes for the first car onto the car guide
car1 = carguide()
car1.name = "Tesla Model X"
car1.kind = "SUV"
car1.colour = "Black"
car1.value = 100000.00
#adds attributes for the second car onto the car guide
car2 = carguide()
car2.name = "Mclaren P20"
car2.kind = "Supercar"
car2.colour = "Orange"
car2.value = 120000.00

print("Which car would you like to know about?")
print("Press 1 for Tesla Model X or Two for Mclaren P20")
choice = int(input())

if choice == 1:
    print(car1.description())
elif choice == 2:
    print(car2.description())
else:
    print("Invalid!")


class StudentRecord():
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

p1 = StudentRecord("Abdi",16,7)
print(p1.name)
print(p1.age)
print(p1.grades)

StudentRecord.grades = 7,7
print(p1.grades)
