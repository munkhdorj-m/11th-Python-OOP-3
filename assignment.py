# assignment.py

# ---------- Exercise 1: School Management System ----------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return "{} (Age: {})".format(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, grade_level):
        super().__init__(name, age)
        self.grade_level = grade_level
        self.marks = []

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
    
    def get_info(self):
        return "{} (Age: {}) — Grade: {}".format(self.name, self.age, self.grade_level)


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.__salary = salary

    def raise_salary(self, amount):
        self.__salary += amount
    
    def get_info(self):
        pass

class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def get_info(self):
        return "{} (Age: {}) — Position: {}".format(self.name, self.age, self.position)


class School:
    def __init__(self):
        self.people = []

    def add_person(self, p):
        self.people.append(p)
    
    def show_all(self):
        for p in self.people:
            print(p.get_info())
    
    def find(self, name):
        for p in self.people:
            if p.name == name:
                return p
        return None


# ---------- Exercise 2: RPG Game System ----------

class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100

    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0

    def heal(self, amount):
        self.__health += amount
        if self.__health > 100:
            self.__health = 100

    def is_alive(self):
        return self.__health > 0

    def get_health(self):
        return self.__health

    def attack(self):
        return 0  # to be overridden


class Warrior(Character):
    def attack(self):
        return 10

    def power_strike(self):
        return 25


class Archer(Character):
    def attack(self):
        return 10

    def double_shot(self):
        return 16


class Mage(Character):
    def attack(self):
        return 5

    def fireball(self):
        return 20
