#!/usr/bin/python

import math

""" 
Object oriented interpretation of Circles bound by a square.
"""

class Point(object):
    """
    Point object which can store its co-ordinates and can represent itself as a 
    '#' or a '.' based on its distance from the outer or the inner circles.
    """
    def __init__(self, x, y, bounding_box):
        self.x = x
        self.y = y
        self.bounding_box = bounding_box
        # Calculate the distance to the midpoint of the bounding box using the Pythagorean theorm.
        self.distance_to_center = math.sqrt(pow((x-bounding_box.mid_point),2)+pow((y-bounding_box.mid_point),2))
    
    def __str__(self):
        default_str = "#"
        if self.distance_to_center < self.bounding_box.outer_circle_dia:
            default_str = "."
        if self.distance_to_center <= self.bounding_box.inner_circle_dia:
            default_str = "#"
        return default_str
    

class BoundingSquare(object):
    """
    A bounding box which defines the drawing logic, and calculates the
    diameters of the outer and the inner circles.
    """
    def __init__(self, side_length):
        self.side_length = side_length
        self.mid_point = self.side_length/2
        self.outer_circle_dia = self.mid_point - 2
        self.inner_circle_dia = self.outer_circle_dia - 3
        # create a points generator which can be used at a later point in time
        self.points = self.calculate_points()

    def calculate_points(self):
        """
        Method which returns a generator for calculating the points for each row
        """
        for i in range(self.side_length+1):
            columns = []
            for j in range(self.side_length+1):
                columns.append(Point(i, j, self))
            yield columns

    def __str__(self):
        output = ""
        for i, each in enumerate(self.points):
            output += "".join(map(str, each)) + "\n"
        return output

if __name__ == "__main__":
    square = BoundingSquare(40)
    print (square)
