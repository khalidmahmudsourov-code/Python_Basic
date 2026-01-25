
# class student():
#     print("Khalid Mahmud Sourov:")

#     def __init__(self,names,marks):
#         self.names = names
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for el in self.marks:
#             sum += el
#         print("Your Average is",sum/3)
#     def display(self):
#         for name in self.names:
#             print(name)
#         for mark in self.marks:
#             print(mark)            

# s1 = student(["Mat361","Mat350","Ben205"],[95,96,97])
# s1.display()
# s1.get_avg()
# s1.marks = [80,75,85]
# s1.get_avg()
################Bank Debit Credit Display
# class Account:
#     balance = 0
#     accountno = " "
#     def __init__(self,balance,Accountno):
#         self.balance = balance
#         self.Accountno = Accountno

#     def debit(self,dammount):
#         self.balance = self.balance-dammount
#         print("Debited Balance: ",dammount)
#         #print("Balance after Debit: ",self.balance)

#     def credit(self,cammount):
#         self.balance = self.balance + cammount
#         print("Credited ammount: ",cammount)
#         #print("Balance after Credit: ",self.balance)
    
#     @staticmethod
#     def display():
#         print("Present Balance: ",A1.balance)


# A1 = Account(5000,"xxxx")
# A1.debit(300) 
# A1.display()
# A1.credit(2000)
# A1.display() 

# class Circle():
#     def __init__(self,r):
#         self.r = r

#     def get_area(self):
#         print("The area of the circle is: ",((22/7)*self.r**2))

#     def get_perimeter(self):
#         print("The Perimeter of the circle is: ",(2*(22/7)*self.r))

# C1 = Circle(7)
# C1.get_area()
# C1.get_perimeter()   


# class Employee():

#     def __init__(self,role,depertment,salary):
#         self.role = role
#         self.depertment = depertment
#         self.salary = salary

#     def show_details(self):
#         print(self.role)
#         print(self.depertment)
#         print(self.salary,"$")

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

       

#     def show_details1(self):
#         print(self.name)
#         print(self.age)
           
#         super().__init__("ML Engineer","AI",50000)        


# E1 = Engineer("Khalid Mahmud Sourov",28)
# E1.show_details1()
# E1.show_details()

# class Order():
#     def __init__(self,order,price):
#         self.order = order
#         self.price = price

#     def __gt__(self,O2):#Dunder function
#         return self.price>O2.price

# O1 = Order("Pen",10)
# O2 = Order("Eraser",15) 

# print(O1>O2)


        
        