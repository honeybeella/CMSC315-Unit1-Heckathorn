# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment demonstrates object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, shallow copying, and deep copying. I completed the required TODO sections and added a custom extension and an additional edge-case test to demonstrate my understanding of these concepts.

## Implementation

### 1. Parent and Child Classes

I created a `ParentClass` with the instance variables `name` and `age`, along with the class variable `species`. I then created a `ChildClass` that inherits from `ParentClass`. The child class adds `grade` and `hobby` attributes, includes a method to display the student's hobby, and overrides the parent's `display_info()` method to display additional information.

### 2. Namespaces

I created two student objects to demonstrate the difference between class and instance namespaces. The `school` variable is shared through the `ChildClass`, while each student has individual instance attributes. I also added a `favorite_color` attribute to only one student to demonstrate that objects can have different instance attributes.

### 3. Shallow and Deep Copying

I used Python's `copy()` and `deepcopy()` functions to compare how nested data is copied. After adding a score to the original dictionary's nested list, the shallow copy reflected the change because it shared the nested list. The deep copy retained the original scores because its nested list was copied separately.

### 4. Student-Created Extension

I added a `__str__()` method to `ChildClass`. This method displays a student object in readable text when it is passed to `print()`, making the output easier to understand.

### 5. Additional Edge-Case Test

I added a test for a student whose scores list is initially empty. The program successfully displayed the empty list and then added a score of 75. This demonstrated that the program can work with an empty list without requiring special error handling for this valid situation.

## Real-World Application

These concepts could be used in a student information system. A parent class could store information shared by different types of users, while child classes could add role-specific details. Namespaces help keep individual records separate, and copying techniques can be useful when creating records for testing or preserving original data before making changes.

## Discussion Board Reflection

After completing the programming assignment, I will discuss what I learned about inheritance, namespaces, and object copying, the challenges I encountered, and how object-oriented programming compares with procedural programming. I will also explain how maintainability and reusability can reduce duplicated code and make future application development easier.


