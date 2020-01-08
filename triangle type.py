a=input("side a = ")
b=input("side b = ")
c=input("side c = ")
if a==b:
    if b==c:
        print("It is an equilateral triangle.")
    else:
        print("It is an isoceles triangle.")
else:
    if b==c or a==c:
        print("It is an isoceles triangle.")
    else:
        print("It is a scalene triangle.")
