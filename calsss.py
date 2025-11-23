class Mobile:
        pass
m1 = Mobile()
m1.brand = "Apple"
m1.model = "iPhone 13"
m1.price = "999.99"

class Student:
         roll_no = 101
         name = "Muhammad Shafi Ahmed"
         Course = "Python Programming"
         Batch = "02"

S1 = Student()
print("Roll No:", S1.roll_no)


class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def info(self):
        print(self.brand, self.price)
m1 = Mobile("Apple", 1200)
m2 = Mobile("Samsung", 1000)
m3 = Mobile("Realme", 800)
m1.info()
m2.info()
m3.info()

class Laptop:
    name = "dell"
    ram = "8GB"
    price = 70000

L1 = Laptop()
print("Laptop Name :", L1.name)
print("LAptop Ram :", L1.ram)
print("Laptop price :",L1.price)

class Employee:
    def __init__(self, name):
        self.name = name
        self. __salary = 0
    
    def set_salary(self, amount):
        if amount > 0:
            self. __salary = amount
        else:
            print("Salary must be positive")
    def get_salary(self):
        return self. __salary

e1 = Employee(input("Enter Your Name: "))
salary = int(input("Enter Your Salary: ")) # convert to int
e1.set_salary(salary)   # <-- call the method to set salary
print("Employee Salary:", e1.get_salary())

class Student1(person):
    def __init__(self, name, course, roll_no):
        super().__init__(name)
        self.course = course
        self.roll_no = roll_no

p1 = person("Muhammad Shafi Ahmed")
p2 Student1(name=








