#!/usr/bin/env python3
# Created By: Lennon Cehajic
# Date: September 25th, 2026
# This program Calculate the area and perimeter from a length and width.
#
def main():
    # Get the length from the user, and convert it to an integer.
    length = int(input("Enter length of the rectangle (cm): "))

    # Get the width from the user, and convert it to an integer.
    width = int(input("Enter width of the rectangle (cm): "))

    # Calculate the area and perimeter of a rectangle.
    area = length * width
    perimeter = 2 * (length + width)

    # Display the area and perimeter to the user with the proper units.
    print("The area is: {}cm²".format(area))
    print("The perimeter is: {}cm".format(perimeter))


if __name__ == "__main__":
    main()
