'''
Created on 3.10.2018

@author: mikaeltunturi
'''
import math

def distance(x1, y1, x2, y2):
    distance_1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance_1
    
def area(x1, y1, x2, y2):
    area_1 = abs((x1 - x2) * (y1 - y2))
    return area_1

def main():
    x_1 = float(input("Enter the x coordinate of the first point.\n"))
    y_1 = float(input("Enter the y coordinate of the first point.\n"))
    x_2 = float(input("Enter the x coordinate of the second point.\n"))
    y_2 = float(input("Enter the y coordinate of the second point.\n"))
    
    print("The distance of the points is {:.2f}.".format(distance(x_1, y_1, x_2, y_2)))
    print("The area of the rectangle defined by the points is {:.2f}.".format(area(x_1, y_1, x_2, y_2)))
main()
    


