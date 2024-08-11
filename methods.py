#function inside class is method,outside class is function.In python everything is inside class,so there is only method

def sum():      #method declared and defined
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))

    c=a+b
    return c

r1=sum()
print(r1)