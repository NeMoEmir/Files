# class Animal:
#     amount_of_legs = 4
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def eat(self, food):
#         return f'I am eating {food}'
#
#
# a1 = Animal('animal1', 'white')
# a2 = Animal('animal2', 'black')
#
#
# class Dog(Animal):
#     follow_commands = True
#
#     def bark(self):
#         return 'Woof!'
#
#
# class Cat(Animal):
#     follow_commands = False
#
#     def meow(self):
#         return 'Meow'
#
#
# c1 = Cat('cat1', 'red')
# print(c1.name, c1.amount_of_legs)
# d1 = Dog('dog1', 'black')
# print(d1.name, d1.amount_of_legs)
# print(d1.eat('bones'))
# print(c1.eat('fish'))
#
# print(d1.follow_commands)
# print(c1.follow_commands)
#
#
# print(d1.bark())
# print(c1.meow())


"""
Создать класс человек, внутри него создать несколько
аттрибутов и методов + метод инит
Затем создать классы Учитель, Доктор, Банкир
у которых будут свои методы и аттрибуты

create class human which will have several attributes and
methods + init method
and then create teacher, doctor and banker which will have
their own methods and attributes
"""


# class Human:
#     can_walk = True
#     can_talk = True
#     can_fly = False
#     amount_of_parents = 2
#
#     def __init__(self, name, age, phone):
#         self.name = name
#         self.age = age
#         self.phone = phone
#
#     def talk(self):
#         return 'I am talking'
#
#     def sleep(self):
#         return 'Zzzzz'
#
#
# class Doctor(Human):
#     can_heal = True
#
#     def heal(self):
#         return 'You are healed'
#
#
# class Teacher(Human):
#     can_teach = True
#
#     def teach(self):
#         return 'Teaching'
#
#
# class Banker(Human):
#     can_lie = True
#
#     def work(self):
#         return 'Working'
#
#
# t1 = Teacher('Teacher', 20, '+996500500500')
# d1 = Doctor('Doctor', 25, '+996700700700')
# b1 = Banker('Banker', 30, '+996300300300')


class Form:

    def set_values(self, height, width):
        self.height = height
        self.width = width


class Square(Form):
    def area(self):
        return self.height * self.width


class Triangle(Form):
    def area(self):
        return (self.height * self.width) / 2


square = Square()
triangle = Triangle()

square.set_values(5, 6)
triangle.set_values(8, 2)

# print(square.area())
# print(triangle.area())


class Human:
    def __init__(self, name, age, phone, address):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

    def sleep(self):
        return 'I am sleeping'


class Developer(Human):
    def code(self):
        return 'I am coding'


class BackendDeveloper(Developer):
    def create_apis(self):
        return 'API created'


class PythonDeveloper(BackendDeveloper):
    def develop_with_django(self):
        return 'Django used for backend'


class PHPDeveloper(BackendDeveloper):
    def develop_with_laravel(self):
        return 'Laravel used for backend'


class FrontendDeveloper(Developer):
    def code_html(self):
        return 'HTML is done'


python_dev = PythonDeveloper('Pythonist', 25, '+996500500500', 'Bishkek')
php_dev = PHPDeveloper('PHPist', 23, '+996100100100', 'Karaganda')
js_dev = FrontendDeveloper('Frontend', 20, '+996200200200', 'Tokmok')

# print(python_dev.develop_with_django())
# print(python_dev.create_apis())
# print(python_dev.code())
# print(python_dev.sleep())
# print(python_dev.code_html())
#
# print(js_dev.code_html())
# print(js_dev.code())

# print(php_dev.develop_with_laravel())
# print(php_dev.create_apis())
# print(php_dev.code())


"""
Создать класс User, 
Добавить к классу несколько аттрибутов и методов

Создать класс RegisteredUser
Наследуется от User
Добавить к этому классу аттрубут registered = True
Добавить к этому классу метод date_joined, который будет показывать дату,
когда зарегистрировался пользователь

Создать класс ActiveUser
Наследуется от RegisteredUser
Добавить к классу ActiveUser аттрибуты amount_of_posts_made
и метод add_post, 
который при вызове увеличит значение аттрибута amount_of_posts_made на 1
"""
from datetime import datetime


class User:
    allowed_ads = False
    amount_of_purchases = 0

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.date_joined = datetime.now()


class RegisteredUser(User):
    registered = True

    def get_date_joined(self):
        return self.date_joined


class ActiveUser(RegisteredUser):
    amount_of_posts = 0

    def add_post(self):
        self.amount_of_posts += 1
        return self.amount_of_posts


user1 = ActiveUser('user1', 'smth@gmail.com', '123')
user2 = ActiveUser('user2', 'smth2@gmail.com', '1234')
user3 = User('user3', 'smth3@gmail.com', '12345')

print(user1.get_date_joined())
print(user1.add_post())
print(user1.add_post())
print(user2.add_post())
print(user2.add_post())

"""
1) Создать класс Employee, 
2) Создать для класса конструктор со следующими аргументами:
 - Имя, Пол, Возраст, Зар.плата.
3) Создать для класса метод get_employee_info(), который даст всю информацию о рабочем
4) Создать для класса метод promote() с одним аргументом, 
который прибавит к зар.плате сотрудника сумму указанную в аргменте и выведет финальную зар плату
5) Создать 3 экземпляра класса Employee
6) Вызвать метод get_employee_info() для каждого сотрудника
7) Повысить зар плату каждого сотрудника по два раза

-------------------------------------------------------
1) Создать класс Waiter, который наследуется от класса Employee
2) Создать аттрибут dishes_served, значением которого является целое число
3) Создать метод serve_dish(), который будет повышать значение dishes_served на 1,
каждый раз, когда будет вызываться метод
4) Повышать зар плату официанту, каждый раз, как у официанта аттрибут dishes_served будет повышаться на 10 раз


------------------------------------------------------------
1) Создать класс Cook, который наследуется от класса Employee
2) Добавить к классу четыре аттрибута - junior_cook, middle_cook, senior_cook, chief, все равны False
3) Создать метод learn_new_recipe(), который будет принимать в аргумент строку
4) При вызове метода learn_new_recipe(), новое блюдо, будет добавлено в список выученных рецептов приготовления
5) Если количество блюд будет равна 3, то повышаем зар плату повара, и даем ему должность junior_cook
6) Если количество блюд  равна или меньше 5, то повышаем зар плату повара и даем ему должность middle_Cook
7) Если количество блюд равна или меньше 7, то повышаем зар плату повара и даем ему должность senior_cook
8) Если количесвто блюд равна или больше 10, то повышаем зар плату повара и даем ему должность chief

------------------------------------------------------------

"""

