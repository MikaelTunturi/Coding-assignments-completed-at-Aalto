'''
@author: mikaeltunturi
'''

import math

def is_inside_circle(x1, y1, circle_x, circle_y, circle_r):
    if distance(x1, y1, circle_x, circle_y) <= circle_r:
        return True
    else:
        return False

def is_inside_rectangle(x1, y1, left_x, lower_y, right_x, upper_y):
    if x1 >= left_x and x1 <= right_x and y1 >= lower_y and y1 <= upper_y:
        return True
    else:
        return False

def distance(x1, y1, x2, y2):
    distance_1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance_1

def check_corners(corner1_x, corner1_y, corner2_x, corner2_y):
    if corner1_x < corner2_x:
        left_x = corner1_x
        right_x = corner2_x
        second_left_y = corner2_y
        second_right_y = corner1_y
        if second_left_y <= corner1_y:
            lower_y = second_left_y
            upper_y = corner1_y
        else:
            lower_y = corner1_y
            upper_y = second_left_y
        return [left_x, lower_y, right_x, upper_y]
    else:
        left_x = corner2_x
        right_x = corner1_x
        second_left_y = corner1_y
        second_right_y = corner2_y
        if second_left_y <= corner2_y:
            lower_y = second_left_y
            upper_y = corner2_y
        else:
            lower_y = corner2_y
            upper_y = second_left_y 
        return [left_x, lower_y, right_x, upper_y]
    
def read_coordinates():
    x = float(input("x coordinate:\n"))
    y = float(input("y coordinate:\n"))
    return (x, y)
    
def main():
    print("Enter the coordinates of the center of the circle.")
    circle_x = float(input("x coordinate:\n"))
    circle_y = float(input("y coordinate:\n"))
    circle_r = float(input("Enter the radius of the circle:\n"))
    print("Enter the coordinates of the first corner of the rectangle.")
    corner1_x = float(input("x coordinate:\n"))
    corner1_y = float(input("y coordinate:\n"))
    print("Enter the coordinates of the second corner of the rectangle.")
    corner2_x = float(input("x coordinate:\n"))
    corner2_y = float(input("y coordinate:\n"))
    koordinaattien_lkm = int(input("How many points are you going to input?\n"))
    for i in range(1, koordinaattien_lkm + 1):
        print("Enter the coordinates of the next point.")
        x,y = read_coordinates()
    inside_circle = 0
    inside_rectangle = 0
    left_x, right_x, lower_y, upper_y = check_corners(corner1_x, corner1_y, corner2_x, corner2_y)
    if is_inside_circle(x, y, circle_x, circle_y, circle_r) == True:
        inside_circle = inside_circle + 1
    if is_inside_rectangle(x, y, left_x, lower_y, right_x, upper_y) == True:   
        inside_rectangle = inside_rectangle + 1
    print(inside_circle, "points were inside the circle.")
    print(inside_rectangle, "points were inside the rectangle.")  
main()
