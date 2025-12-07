import pytest
from assignment import Shape, Rectangle, Animal, Dog, Employee, Manager


# ---------------------------------------------------
# Exercise 1 — Shape → Rectangle
# ---------------------------------------------------
@pytest.mark.parametrize(
    "name,width,height,expected_area",
    [
        ("Box", 4, 6, 24),
        ("Big", 10, 10, 100),
        ("Flat", 8, 1, 8),
    ]
)
def test1(name, width, height, expected_area):
    r = Rectangle(name, width, height)
    assert r.get_name() == name
    assert r.area() == expected_area


# ---------------------------------------------------
# Exercise 2 — Animal → Dog
# ---------------------------------------------------
@pytest.mark.parametrize(
    "animal_obj,expected_sound",
    [
        (Animal(), "Some sound"),
        (Dog(), "Bark"),
    ]
)
def test2(animal_obj, expected_sound):
    assert animal_obj.sound() == expected_sound


# ---------------------------------------------------
# Exercise 3 — Employee → Manager
# ---------------------------------------------------
@pytest.mark.parametrize(
    "name,salary,bonus,expected_total",
    [
        ("Alice", 1000, 200, 1200),
        ("Bob", 1500, 0, 1500),
        ("Cara", 900, 300, 1200),
    ]
)
def test3(name, salary, bonus, expected_total):
    m = Manager(name, salary, bonus)

    # base class method
    assert m.get_salary() == salary

    # derived class method
    assert m.total_salary() == expected_total
