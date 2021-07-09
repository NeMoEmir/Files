# class Student:
#     pass
#
#
# student1 = Student()
# student2 = Student()
#
# print(student1)
# print(student1)
#
# student1.name = 'Dima'
# student1.email = 'dima@gmail.com'
# student1.age = 16
#
# student2.name = 'Emir'
# student2.email = 'emirbay_3579@mail.com'
# student2.age = 13
#
# print(student1.name, student1.email, student1.age)
# print(student2.name, student2.email, student2.age)
#
# class Employee:
#    def __init__(self, name, email, age):
#       self.name = name
#       self.email = email
#       self.age = age
#
#    def get_info(self):
#       return f'{self.name}, {self.email}, {self.age}'
#
#    def check_age(self):
#       return 'Not 18 yet' if self.age < 18 else 'legal to work'
#
#
# employee1 = Employee('Dima', 'dima@gmail.com', 16)
# employee2 = Employee('Emir', 'emirbay_3579@mail.com', 13)
#
# print(employee1.name, employee1.email, employee1.age)
# print(employee2.name, employee2.email, employee2.age)
#
# print(employee1.get_info())
# print(employee2.get_info())
#
#
# class Dog:
#    friends = []
#
#    def __init__(self, name, breed, color):
#       self.name = name
#       self.breed = breed
#       self.color = color
#
#    def get_info(self):
#       return f'{self.name} {self.breed} {self.color}'
#
#    def bark(self):
#       return 'woof woof'
#
#    def eat(self, food):
#       return f'woof {food} is woofy delicious!!'
#
#    def make_friend(self, friend):
#       self.friend.append(friend)
#       friend.friends.append(self)
#
# haski = Dog('Hachiko', 'haski', 'Gray')
# retriever = Dog('beathoven', 'retriever', 'Blue')
# pudel = Dog('Cloud', 'pudel', 'Pink')
#
# # print(haski.amount_of_legs)
# # print(retriever.amount_of_legs)
#
# print(haski.get_info())
# print(haski.bark())
# print(haski.eat('Steak'))
# haski.make_friend(retriever)
# print(haski.friend.name)
# print(haski)

# class Animal:
#     amout_of_legs = 4
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def eat(self, food):
#         return  f'I am eating {food}'
#
# a1 = Animal('animal1', 'Blue')
# a2 = Animal('animal2', 'Green')
#
# class Dog(Animal):
#     comands = True
#
#     def bark(self):
#         return 'Woof!'
#
#
# class Cat(Animal):
#     comands = False
#
#     def meow(self):
#         return 'Meow!'
#
# c1 = Cat('Yolka', 'Black')
# c2 = Cat('Muha', 'Gray')
# d1 = Dog('Tyaftel', 'White')
# print(d1)
# print(c1.name, c1.amout_of_legs)
# print(c2.name, c2.amout_of_legs)
# print(d1.eat('Steak'))
# print(d1.eat('Fish'))
# print(d1.comands)
# print(c1.comands)
# print(d1.bark())
# print(c1.meow())

# class Human:
#     can_walk = True
#     can_talk = True
#
#     def __init__(self, name, age, health_status):
#         self.age = age
#         self.health_status = health_status
#         self.name = name
#
#     def talk(self):
#         return 'I am talkin Bla bla bla'
#
#     def sleeping(self):
#         return 'Zzzz'
#
#
# class Gardener_in_Minecraft:
#     can_playing_Minecraft = True
#
#
#     def canplayingMinecraft(self):
#         return 'DIAMONDS'
#
#
# class Programmer:
#     fast_typing = True
#
#     def typing(self):
#         return 'NeMo'
#
#
# class Electrick:
#     can_fix = True
#     def fixing(self):
#         return 'F***'

# class Form:
#
#     def set_values(self, height, width):
#         self.height = height
#         self.width = width
#
# class Square(Form):
#     def area(self):
#         return self.height * self.width
#
# class Triangle(Form):
#     def area(self):
#         return (self.height * self.width) / 2
#
# square = Square()
# triangle = Triangle()
#
# square.set_values(5, 6)
# triangle.set_values(8, 6)
#
# print(square.area())
# print(triangle.area())

# class Human:
#     def __init__(self, name, age, phone, address):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         self.address = address
#
#     def sleep(self):
#         return 'Zzzzz'
#
#
# class Developer(Human):
#     def code(self):
#         return 'I am coding'
#
#
# class BackendDeveloper(Developer):
#     def creat_apis(self):
#         return 'API created'
#
#
# class PythonDeveloper(BackendDeveloper):
#     def develop_with_django(self):
#         return 'Django used for backend'
#
#
# class PHPDeveloper(BackendDeveloper):
#     def developer_with_laravel(self):
#         return 'Laravel used for backend'
#
#
# class FrontendDeveloper(Developer):
#     def code_html(self):
#         return 'HTML is done'
#
#
# python_dev = PythonDeveloper('Pythonist', 25, '+996701188159', 'Bishkek')
# php_dev = PHPDeveloper('PHPist', 24, '+996701188156', 'Bishkek')
# js_dev = FrontendDeveloper('Frontend', 20, '+996701188155', 'Bishkek')
# print(python_dev.develop_with_django())
# print(python_dev.create_apis())
# print(python_dev.code())
# print(php_dev.developer_with_laravel())
# print(php_dev.create_apis())
# print(php_dev.code())
# print(python_dev.sleep)

# from datetime import datetime
#
# class User:
#     allowed_adds = False
#     amout_of_purshases = 0
#
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.datetime = datetime.now()
#
# class RegisteredUser(User):
#     registered = True
#
#     def get_data_joined(self):
#         return self.data_joined
#
# class ActiveUser(RegisteredUser):
#     amout_of_posts = 0
#
#     def add_post(self):
#         self.amout_of_posts += 1
#         return  self.amout_of_posts
#
# user1 = ActiveUser('user1', 'atwdasa@gmail.com', '123')
# user2 = ActiveUser('user2', 'wadsadwas@gmail.com', '213')
# user3 = User('user3', 'wadswdas@gmail.com', '12312321')
#
# print(user1.get_data_joined())
# print(user1.add_post())
# print(user1.add_post())

# class Employee:
#     def __init__(self, name, gender, age, salary):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.salary = salary
#
#     def get_info_employee(self):
#         return self.name, self.gender, self.age, self.salary
#
#     def promote(self, increase_salary):
#         return self.salary + increase_salary
#
#     def promote2(self, increase_salary):
#         return self.salary + increase_salary + increase_salary
#
#
# class Waiter(Employee):
#     dishes_served = 0
#
#     if dishes_served == 10:
#         print(Employee.promote(500))
#
#
# E1 = Employee('Emir', 'Male', 13, 20000)
# E2 = Employee('Danil', 'Male', 12, 25000)
# E3 = Employee('Askar', 'Male', 12, 25000)
# W1 = Waiter('Madara', 'Female', 56, 10000)
# print(E1.get_info_employee())
# print(E2.get_info_employee())
# print(E3.get_info_employee())
# print(W1.get_info_employee())
# print(E1.promote2(3000))
# print(E1.promote2(3000))
# print(E1.promote2(3000))
# print(W1.promote(10000))

# class A:
#     x = 5
#
#
# class B:
#     x = 10
#
#
# class C(A, B):
#     pass
#
#
# c = C()
# # print(c.x)
#
#
# class Donkey:
#     is_donkey = True
#
#
# class Horse:
#     is_horse = True
#
#
# class Mule(Donkey, Horse):
#     pass
#
#
# mule = Mule()
# print(mule.is_horse)
# print(mule.is_donkey)
#
#
# class Transport:
#
#     def drive(selfself):
#         print('driving')
#
#     def carry_goods(self):
#         print('carrying goods')
#
#
# class Car(Transport):
#
#     def carry_passangers(self):
#         print('carrying passengers')
#
#
# class CraneMixin:
#
#     def lift(self):
#         print('lifting something')
#
#
# class TrunkWithCrane(Transport, CraneMixin):
#
#     def carry_things(self):
#         print('carrying things')
#
#
# class MotorBoatWithCrane(Transport, CraneMixin):
#
#     def dock(self):
#         print('docked')


# class PhoneMixin:
#     def call(self):
#         return 'Calling...'
#
#
# class Technology:
#     def charge(self):
#         return 'I am charging'
#
#
# class MobilePhone(PhoneMixin, Technology):
#     can_playing = True
#     saved_phones = 3
#
#     def map(self):
#         return 'locating your position'
#
#
# class HomePhone(PhoneMixin, Technology):
#     can_playing = False
#     saved_phones = 6
#
#     def saving_phone(self):
#         return 'Phone number saved'
#
#
# class Computer(Technology):
#     can_playing = True
#
#     def coding(self):
#         return 'Coding'
#

# class BlazeRod:
#     pass
#
# class BlazePowder(BlazeRod):
#     def EyeOfEnder(self):
#         return 'Craft'

# class Horse:
#     can_milk = True
#
#
# class Donkey:
#     can_milk = False
#
#
# class Mule(Horse, Donkey):
#     can_milk = False
#
#
# m = Mule
# print(m.can_milk)


# class Form:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return f'{self.a}, {self.b}'
#
#
# class Square(Form):
#     def area(self):
#         return self.a * self.b
#
#
# class Rectangle(Form):
#     def area(self):
#         return (self.a + self.b) * 2
#
#
# class Circle(Form):
#     pass
#
#
# square = Square(4, 5)
# rectangle = Rectangle(2, 3)
# circle = Circle(8, 7)

# print(square.area())
# print(rectangle.area())
# print(circle.area())

# class Pizza:
#     def __init__(self, size, ingredients):
#         self.size = size
#         self.ingredients = ingredients
#
#
# class Margharita(Pizza):
#     def __init__(self):
#         super().__init__(30, ['Tomato', 'oreghano'])
#
# class FourCheese(Pizza):
#     def __init__(self):
#         super().__init__(23, ['moccarela', 'cheese', 'cheese2'])
#
#
# pizza = Pizza(25, ['mushrooms', 'chicken'])
# margharita = Margharita()
# four_cheese = FourCheese()
#
#
# print(pizza.ingredients)
# print(margharita.ingredients)
# print(four_cheese.ingredients)

# class MinePlayer:
#     def __init__(self, intelligence, armor, tools):
#         self.intelligence = intelligence
#         self.armor = armor
#         self.tools = tools
#
#     def get_player_info(self):
#         return f'{self.intelligence}, {self.armor}, {self.tools}'
#
#
# class Villager(MinePlayer):
#     def __init__(self):
#         super().__init__('low', 'none', 'none')
#
#
# player = MinePlayer('High', 'Netherite', 'Netherite')
# villager = Villager()

# print(dir(1))

# class CInt:
#     def __init__(self, n):
#         self.n = n
#
#     def __add__(self, other):
#         return f'Sum is {self.n + other}'
#
#     def __eq__(self, other):
#         if self.n == other:
#             return f'{self.n} is equal to {other}'
#         else:
#             return f'{self.n} is not equal to {other}'

