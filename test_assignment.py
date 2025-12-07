# test_assignment.py
import pytest
from assignment import Student, Teacher, Staff, School
from assignment import Warrior, Archer, Mage

# ---------- Test School Management System ----------

@pytest.mark.parametrize("name, age, grade_level, marks, expected_avg", [
    ("Alice", 16, 11, [90, 85, 95], 90.0),
    ("Bob", 15, 10, [70, 80, 90], 80.0),
    ("Charlie", 17, 12, [], 0),
])
def test_student_average(name, age, grade_level, marks, expected_avg):
    s = Student(name, age, grade_level)
    s.marks = marks
    assert s.calculate_average() == expected_avg

def test_teacher_salary_and_info():
    t = Teacher("Tom", "Physics",30, 1000)
    t.raise_salary(0)
    assert t.get_salary() == 1000  
    t.raise_salary(200)
    assert t.get_salary() == 1200

def test_staff_info():
    st = Staff("Janitor Joe", 50, "Janitor")
    assert st.get_info() == "Janitor Joe (Age: 50) — Position: Janitor"

def test_school_add_and_find():
    school = School()
    s = Student("Alice", 16, 11)
    t = Teacher("Mr. Brown", 40, "Math", 1200)
    st = Staff("Janitor Joe", 50, "Janitor")
    
    school.add_person(s)
    school.add_person(t)
    school.add_person(st)
    
    assert school.find("Alice") == s
    assert school.find("Mr. Brown") == t
    assert school.find("Janitor Joe") == st
    assert school.find("Ghost") == None

# ---------- Test RPG Game System ----------

@pytest.mark.parametrize("damage, expected_health", [
    (10, 90),
    (50, 50),
    (120, 0),
])
def test_take_damage(damage, expected_health):
    w = Warrior("Thor")
    w.take_damage(damage)
    assert w.get_health() == expected_health

@pytest.mark.parametrize("heal_amount, initial_health, expected_health", [
    (20, 50, 70),
    (100, 50, 100),
    (10, 95, 100),
])
def test_heal(heal_amount, initial_health, expected_health):
    m = Mage("Gandalf")
    m.take_damage(100 - initial_health)  # reduce to initial_health
    m.heal(heal_amount)
    assert m.get_health() == expected_health

def test_is_alive_and_attack():
    a = Archer("Legolas")
    assert a.is_alive() == True
    a.take_damage(100)
    assert a.is_alive() == False
    assert a.attack() == 10
    assert a.double_shot() == 16

def test_warrior_special():
    w = Warrior("Conan")
    assert w.attack() == 10
    assert w.power_strike() == 25

def test_mage_special():
    m = Mage("Merlin")
    assert m.attack() == 5
    assert m.fireball() == 20
