def compute_area_of_rect(b: float, c: float):
    return b * c


b = float(input("Side a: "))
c = float(input("Side b: "))

print(f"The area of the rectangle is {compute_area_of_rect(b,c)}")
