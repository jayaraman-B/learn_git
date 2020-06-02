r=int(input("Enter the Radius of the circle:"))
h=int(input("Enter the height of the cylindr:"))

def area(r):
    area=round(3.14*r*r,2)
    print("Area of the circle is ",area)

def perimeter(r):
    perimeter=round(2*3.14*r,2)
    print("Area of the perimeter is",perimeter)

def cylinder_area(r,h):
    area=round(3.14*r*r*h,2)
    print("Area of the cylinder is ",area)

    
area(r)
perimeter(r)
cylinder_area(r,h)
