
"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

This assignment demonstrates object-oriented programming,
inheritance, namespaces, shallow copying, and deep copying.
"""

from copy import copy, deepcopy


# TODO 1: Create a parent class.
class ParentClass:
    # Class variable shared by all ParentClass objects
    species = "Human"

    def __init__(self, name, age):
        # Instance variables unique to each object
        self.name = name
        self.age = age

    # Display the object's information
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# TODO 2: Create a child class that inherits from ParentClass.
class ChildClass(ParentClass):
    # Class variable shared by ChildClass objects
    school = "Python Academy"

    def __init__(self, name, age, grade, hobby):
        # Initialize inherited variables
        super().__init__(name, age)

        # Add child-specific instance variables
        self.grade = grade
        self.hobby = hobby

    # Display the student's hobby
    def display_hobby(self):
        return f"{self.name}'s hobby is {self.hobby}."

    # Override the parent's display_info() method
    def display_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Grade: {self.grade}, Hobby: {self.hobby}"
        )

    # Student-created extension: readable object representation
    def __str__(self):
        return (
            f"Student: {self.name}, "
            f"Grade: {self.grade}, "
            f"Hobby: {self.hobby}"
        )


# TODO 3: Demonstrate class and instance namespaces.
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two ChildClass objects
    student1 = ChildClass("Bella", 18, "12th Grade", "Reading")
    student2 = ChildClass("David", 17, "11th Grade", "Gaming")

    # Access a class variable through the class and an object
    print("Class variable through class:", ChildClass.school)
    print("Class variable through object:", student1.school)

    # Add an attribute to only the first student
    student1.favorite_color = "Blue"

    # Display each object's instance namespace
    print("\nStudent 1 instance namespace:")
    print(student1.__dict__)

    print("\nStudent 2 instance namespace:")
    print(student2.__dict__)

    # Display the class namespace
    print("\nChildClass namespace:")
    print(ChildClass.__dict__)


# TODO 4: Demonstrate shallow and deep copying.
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object containing nested mutable data
    original = {
        "name": "Bella",
        "scores": [85, 90, 95]
    }

    # A shallow copy creates a new outer dictionary,
    # but the nested list is shared with the original.
    shallow_copy = copy(original)

    # A deep copy creates a separate copy of the nested list.
    deep_copy = deepcopy(original)

    # Modify the nested list in the original dictionary
    original["scores"].append(100)

    # Display the results of the copying demonstration
    print("Original object:", original)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep_copy)

    # Additional test case: a student with no scores
    empty_student = {
        "name": "New Student",
        "scores": []
    }

    print("\n=== Edge Case: Empty Scores ===")
    print("Student with no scores:", empty_student)

    # Confirm that an empty list can accept its first score
    empty_student["scores"].append(75)
    print("Student after adding first score:", empty_student)


# TODO 5: Complete the main function.
def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object
    print("\n=== Parent Object ===")
    parent = ParentClass("Douglass", 40)
    print(parent.display_info())
    print("Species:", parent.species)

    # Create and test a child object
    print("\n=== Child Object ===")
    child = ChildClass("Bella", 18, "12th Grade", "Reading")
    print(child.display_info())
    print(child.display_hobby())
    print("School:", child.school)

    # Demonstrate the student-created extension
    print("\n=== Student-Created Extension ===")
    print(child)

    # Demonstrate inheritance from the parent class
    print("\n=== Inheritance Demonstration ===")
    print("Child inherits species:", child.species)
    print("Child inherits name:", child.name)

    # Run the namespace and copying demonstrations
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()

