# WAF to make a calculator 
"""import math
# addition
def sum(a,b):
    return (a+b)
# subtraction
def sub(a,b):
    return (a-b)
# multiply
def multi(a,b):
    return (a*b)
# division
def div(a,b):
    return (a/b)
# sqaure root
def sqrt(a):
    return math.sqrt(a)
# power
def power(a,b):
    return math.pow(a,b)
# sinQ
def sin(a):
    a= (a*3.14)/180
    return math.sin(a)
# cosQ
def cos(a):
    a= (a*3.14)/180
    return math.cos(a)
# Menu
def menu():
    print("Menu / 1:add / 2:sub / 3:multiply / 4:divide / 5:power / 6:sqrt / 7:sin / 8:cos")
    choice= int(input("Enter your choice: "))
    match(choice):
        case 1:
            print("You have selected to add")      
            a= int(input("enter a number: "))
            b= int(input("enter a number: "))
            print(sum(a,b))
        case 2:
            print("You have selected subtract")      
            a= int(input("enter a number: "))
            b= int(input("enter a number: "))
            print(sub(a,b))
        case 3:
            print("You have selected mutiply")       
            a= int(input("enter a number: "))
            b= int(input("enter a number: "))
            print(multi(a,b))
        case 4:
            print("You have selected divide")
            a= int(input("enter a number: "))
            b= int(input("enter a number: "))
            print(div(a,b))
        case 5:
            print("You have selected power")
            a= int(input("enter a number to  be powered: "))
            b= int(input("enter a number to power with: "))
            print(power(a,b))
        case 6:
            print("You have selected Square root")
            a =int(input("enter a number: "))
            print(sqrt(a))
        case 7:
            print("You have selected sin ")
            a= int(input("enter an angle: "))
            print(sin(a))
        case 8:
            print("You have selected cos ")
            a= int(input("enter an angle: "))
            print(cos(a))
        case _:
            print("Invalid option")
            menu()
    return

menu()"""

# Another way with a function to print input
# store the return values of def print_2() as they are local variable 
# WAF to make a calculator 
"""import math
# addition
def sum(a,b):
    return (a+b)
# subtraction
def sub(a,b):
    return (a-b)
# multiply
def multi(a,b):
    return (a*b)
# division
def div(a,b):
    return (a/b)
# sqaure root
def sqrt(a):
    return math.sqrt(a)
# power
def power(a,b):
    return math.pow(a,b)
# sinQ
def sin(a):
    a= (a*3.14)/180
    return math.sin(a)
# cosQ
def cos(a):
    a= (a*3.14)/180
    return math.cos(a)

def print_2():
    a= int(input("enter a number: "))
    b= int(input("enter a number: "))
    return a, b
# Menu
def menu():
    print("Menu / 1:add / 2:sub / 3:multiply / 4:divide / 5:power / 6:sqrt / 7:sin / 8:cos")
    choice= int(input("Enter your choice: "))
    match(choice):
        case 1:
            print("You have selected to add")      
            a,b=print_2()
            print(sum(a,b))
        case 2:
            print("You have selected subtract")      
            a,b=print_2()
            print(sub(a,b))
        case 3:
            print("You have selected mutiply")       
            a,b=print_2()
            print(multi(a,b))
        case 4:
            print("You have selected divide")
            a,b=print_2()
            print(div(a,b))
        case 5:
            print("You have selected power")
            a,b=print_2()
            print(power(a,b))
        case 6:
            print("You have selected Square root")
            a =int(input("enter a number: "))
            print(sqrt(a))
        case 7:
            print("You have selected sin ")
            a= int(input("enter an angle: "))
            print(sin(a))
        case 8:
            print("You have selected cos ")
            a= int(input("enter an angle: "))
            print(cos(a))
        case _:
            print("Invalid option")
            menu()
    return

menu()"""



# Calcula
# tor using lambda function

"""import math

def print_2():
    a= int(input("enter a number: "))
    b= int(input("enter a number: "))
    return a, b
# Menu
def menu():
    print("Menu / 1:add / 2:sub / 3:multiply / 4:divide / 5:power / 6:sqrt / 7:sin / 8:cos")
    choice= int(input("Enter your choice: "))
    match(choice):
        case 1:
            print("You have selected to add")      
            a,b=print_2()
            res= (lambda a,b :a+b)(a,b)
            print(res)
        case 2:
            print("You have selected subtract")      
            a,b=print_2()
            res= (lambda a,b :a-b)(a,b)
            print(res)
        case 3:
            print("You have selected mutiply")       
            a,b=print_2()
            res= (lambda a,b :a*b)(a,b)
            print(res)
        case 4:
            print("You have selected divide")
            a,b=print_2()
            res= (lambda a,b :a/b)(a,b)
            print(res)
        case 5:
            print("You have selected power")
            a,b=print_2()
            res= (lambda a,b :math.pow(a,b))(a,b)
            print(res)
        case 6:
            print("You have selected Square root")
            a =int(input("enter a number: "))
            res= (lambda a :math.sqrt(a))(a)
            print(res)
        case 7:
            print("You have selected sin ")
            a= int(input("enter an angle: "))
            a= (a*3.14)/180
            res= (lambda a :math.sin(a))(a)
            print(res)
        case 8:
            print("You have selected cos ")
            a= int(input("enter an angle: "))
            a= (a*3.14)/180
            res= (lambda a :math.cos(a))(a)
            print(res)
        case _:
            print("Invalid option")
            menu()
    return

menu()"""









