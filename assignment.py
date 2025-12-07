# ---------- Exercise 1: School Management System ----------

class Person:
    def __init__(self, name, age):
        pass
    
    def get_info(self):
        pass


class Student(Person):
    def __init__(self, name, age, grade_level):
        pass

    def calculate_average(self):
        pass
    
    def get_info(self):
        pass


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        pass

    def raise_salary(self, amount):
        pass
    
    def get_info(self):
        pass

class Staff(Person):
    def __init__(self, name, age, position):
        pass

    def get_info(self):
        pass


class School:
    def __init__(self):
        pass

    def add_person(self, p):
        pass
    
    def show_all(self):
        pass
    
    def find(self, name):
        pass


# ---------- Exercise 2: RPG Game System ----------

class Character:
    def __init__(self, name):
        pass

    def take_damage(self, amount):
        pass

    def heal(self, amount):
        pass

    def is_alive(self):
        pass

    def get_health(self):
        pass

    def attack(self):
        pass


class Warrior(Character):
    def attack(self):
        pass

    def power_strike(self):
        pass

class Archer(Character):
    def attack(self):
        pass

    def double_shot(self):
        pass


class Mage(Character):
    def attack(self):
        pass

    def fireball(self):
        pass
