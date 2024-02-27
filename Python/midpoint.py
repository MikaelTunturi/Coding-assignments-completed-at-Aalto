'''
Created on 31.10.2018

@author: mikaeltunturi
'''

from builtins import list

def read_points():
    print("Input the points, one per line as x,y.")
    print("Stop by entering an empty line.")
    
    points = input("")
    points = points.split(",")
    
    pointslist = []
    
    if len(points) > 1:
        while len(points) > 1:
            points_as_float = []
            for i in points:
                i = float(i)
                points_as_float.append(i)
            pointslist.append(points_as_float)
            points = input("")
            points = points.split(",")
        return pointslist
    else:
        return pointslist
        
def calculate_midpoint(pointslist):
    x = 0
    y = 0
    i = 0
    for alkio in pointslist:
        x = x + float(alkio[0])
        y = y + float(alkio[1])
        i = i + 1
    x_mid = x / i
    y_mid = y / i
    midpoint = []
    midpoint.append(x_mid)
    midpoint.append(y_mid)
    return midpoint
        
def above_point(list_of_points, y_limit):
    points_above = 0
    for i in list_of_points:
        if i[1] > y_limit:
            points_above += 1
    return points_above

def main():
    pointslist = read_points()
    if len(pointslist) > 0:
        midpoint = calculate_midpoint(pointslist)
        list_of_points = pointslist
        y_limit = midpoint[1]
        points_above = above_point(list_of_points, y_limit)

        print("The midpoint is ({:.2f}, {:.2f}).".format(midpoint[0], midpoint[1]))
        print("The number of points above the midpoint is {:d}.".format(points_above))
    else:
        print("You did not input any points.")
    
main()