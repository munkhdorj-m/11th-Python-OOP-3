# Object Oriented Programming (Inheritance)

OOP PDF:

https://drive.google.com/file/d/1Dfu8jYSOsRFwReeNXO6nA0ffTYqtH2BT/view?usp=sharing

---

## Exercise 1

**Problem:**
 
Build a mini game engine system for an RPG.

Requirements:  

Base Class (Parent class): Character   
Attributes:   
* name
* __health (private)
    * Always between 0 and 100

Example:

    Input:
        r = Rectangle("MyRect", 4, 6)
        print(r.get_name())
        print(r.area())
    
    Output:
        MyRect
        24

  
---

## Exercise 2

**Problem:**
Create a base class `Animal` with a `sound()` method.   
Create a derived class `Dog` that overrides the sound.   

Requirements:  

Animal:  
* Method: `sound()` → returns "Some sound"

Dog(Animal):  
* Overridden `sound()` → returns "Bark"


Example:

    Input:
        a = Animal()
        d = Dog()
        print(a.sound())
        print(d.sound())
    
    Output:
        Some sound
        Bark

---

## Exercise 3

**Problem:** 
Create an `Employee` class with a `name` and `salary`.     
Create a `Manager` class that inherits from `Employe`e but includes bonus calculation.   

Requirements:  

Employee:
* `name`
* `salary`
* method: `get_salary()`

Manager(Employee): 
* bonus attribute
* method: `total_salary()` → salary + bonus


Example:

    Input:
        m = Manager("Erdene", 1200, 300)
        print(m.get_salary())
        print(m.total_salary())
    
    Output:
        1200
        1500

---

