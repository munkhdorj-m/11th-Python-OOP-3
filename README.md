# Object Oriented Programming (Inheritance)

OOP PDF:

https://drive.google.com/file/d/1Dfu8jYSOsRFwReeNXO6nA0ffTYqtH2BT/view?usp=sharing

---

## Exercise 1

**Problem:**
Build a mini School Management System.

**Requirements:**

Base Class (Parent class): Person   
Attributes:   
* `name`
* `age`

Methods:  
* `get_info()` - Returns string such as - "Alice (Age: 16)"

Subclasses (Child classes):  

Student:
* Extra attributes:   
    * `grade_level`
    * `marks` (list)
* Methods:
    * `calculate_average()` - return grade average of marks
 
Teacher:   
* Extra attributes:   
    * `subject`
    * `__salary` (private)
* Methods:
    * `raise_salary(amount)` - adds salary
    * `get_salary()` - return salary
 
Staff:   
* Extra attributes:   
    * `position` - (e.g. “Librarian”, “Janitor”)
* Methods:
    * `get_info()` - Returns string such as - "Janitor Joe (Age: 50) - Position: Janitor"

School:  
Acts as a container.  
 
Attributes:  
* `people` - a list of Person objects (students + teachers + staff)   
  
Methods:    
* `add_person(p)` - Add any object of type Person (polymorphism)
* `show_all()` - Loop and call each person’s get_info()
* `find(name)` - Returns the Person with that name, or None

**Example:**

    Input:
        school = School()
        
        t1 = Teacher("Mr. Brown", 40, "Math", 1200)
        s1 = Student("Alice", 16, 11)
        s1.marks = [90, 85, 95]
        
        st1 = Staff("Janitor Joe", 50, "Janitor")
        
        school.add_person(t1)
        school.add_person(s1)
        school.add_person(st1)
        
        school.show_all()
        
        print(school.find("Alice").calculate_average())
    
    Output:
        Mr. Brown (Age: 40) - Subject: Math
        Alice (Age: 16) - Grade: 11
        Janitor Joe (Age: 50) - Position: Janitor
        90.0

---

## Exercise 2

**Problem:**
 
Build a mini game engine system for an RPG.

**Requirements:**

Base Class (Parent class): Character   
Attributes:   
* `name`
* `__health` (private) - Always between 0 and 100

Methods:  
* `take_damage(amount)`
    * Subtract amount from health
    * Health must NOT go below 0

* `heal(amount)`
    * Add amount to health
    * Max health = 100

* `is_alive()`
    * Returns True if health > 0

* `attack()`
    * Returns damage number
    * gets overridden

Subclasses (Child classes):
* Warrior
    * `attack()` → deals 10 damage
    * Special: `power_strike()` - 25 damage
* Archer
    * `attack()` → deals 10 damage
    * Special: `double_shot()` → 16 damage
* Mage
    * `attack()` → deals 5 damage
    * Special: `fireball()` → 20 damage

**Example:**

    Input:
        warrior = Warrior("Thor")
        mage = Mage("Gandalf")
    
        # Round 1
        mage.take_damage(warrior.attack())
        warrior.take_damage(mage.attack())
        mage.take_damage(warrior.power_strike())
        warrior.heal(10)
        mage.heal(5)
    
        # Print status
        print(warrior.get_health())
        print(mage.get_health())
        print(warrior.is_alive())
        print(mage.is_alive())

    Output:
        90
        80
        True
        True
  
---



