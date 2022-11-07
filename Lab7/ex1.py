from math import pi

r = 1


def compute_circumference(r: float):
    return 2 * pi * r


def compute_area(r: float):
    return pi * r**2


print(
    f"For radius = {r}, the circumference is {compute_circumference(r)} and area is {compute_area(r)}"
)
