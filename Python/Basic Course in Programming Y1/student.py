'''
Created on 24.11.2018

@author: mikaeltunturi
'''
# The Student-class represents one student on a course

class Student:

    # The method __init__ initializes attribute values of
    # an object that is being created. The name and student
    # ID are given as parameters to the method.

    def __init__(self, given_name, number):
        self.__name = given_name
        self.__id = number
        self.__examgrade = 0
        self.__assignmentgrade = 0


    # Returns the name of a Student-object

    def get_name(self):
        return self.__name


    # Returns the id of a Student-object

    def get_id(self):
        return self.__id


    # Returns the exam grade of a Student-object

    def get_examgrade(self):
        return self.__examgrade


    # Returns the assignment grade of
    # a Student-object

    def get_assignmentgrade(self):
        return self.__assignmentgrade


    # Changes a student's exam grade. The new grade is
    # given as parameter to the method

    def change_examgrade(self, grade):
        if 0 <= grade <= 5:
            self.__examgrade = grade

    def raise_examgrade(self, new_grade):
        if 5 >= new_grade > self.__examgrade:
            self.__examgrade = new_grade

    # Changes a student's assignment grade. The new
    # grade is given as parameter to the method

    def change_assignmentgrade(self, grade):
        if 0 <= grade <= 5:
            self.__assignmentgrade = grade


    # Calculates and returns a student's final grade

    def calculate_finalgrade(self):
        if self.__examgrade == 0:
            grade = 0
        elif self.__assignmentgrade == 0:
            if self.__examgrade > 2:
                grade = self.__examgrade - 2
            else:
                grade = 0
        elif 1 <= self.__assignmentgrade <= 2:
            if self.__assignmentgrade == 2:
                grade = self.__examgrade - 1
            else:
                grade = 1
        elif self.__assignmentgrade == 3 or self.__assignmentgrade == 4:
            grade = self.__examgrade
                
        elif self.__assignmentgrade == 5:
            if self.__examgrade < 5:
                grade = self.__examgrade + 1
            elif self.__examgrade == 5:
                grade = 5
        return grade

    # returns a string representation of a student

    def __str__(self):
        str1 = self.__name + ", " + self.__id + \
               ", exam grade: " + str(self.__examgrade) + \
               ", assignment grade: " + str(self.__assignmentgrade)
        return str1