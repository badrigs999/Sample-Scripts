#!/usr/bin/python

import math

""" Circles bound by a square """


side_length = 40			                # side length of the outer square
mid_point = side_length/2	                # mid point of the square side-length/2
outer_circle_dia = mid_point - 2            # diameter of the outer circle
inner_circle_dia = outer_circle_dia - 3     # diameter of the inner circle


def main():
    """
    Iteratively walk through every point of the diagram and
    1. Calculate the distance to the center using the Pythagorean theorm.
    2. Draw a #, . depending on where the point lies.
    """
    drawing = ""
    for i in range(side_length+1):
        for j in range(side_length+1):

            # 1. Calculate the distance to the center using the Pythagorean theorm.
            distance_to_center = math.sqrt(pow((i-mid_point),2)+pow((j-mid_point),2))

            # 2. Draw a #, . depending on where the point lies.
            if distance_to_center <= inner_circle_dia:
                drawing += "#"
            elif distance_to_center < outer_circle_dia:
                drawing += "."
            else:
                drawing += "#"
        drawing += "\n"
    print (drawing)


if __name__ == "__main__":
    main()