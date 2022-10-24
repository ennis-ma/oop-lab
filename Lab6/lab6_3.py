triangle = [input("Side 1: "), input("Side 2: "), input("Side 3: ")]
triangle_type = ""
for side in triangle:
    if triangle.count(side) == 3:
        triangle_type = "Equilateral Triangle"
        break
    elif triangle.count(side) == 2:
        triangle_type = "Isosceles Triangle"
        break
    else:
        triangle_type = "Scalene Triangle"
