for i in range(50,90,10):#range(start,stop,step)
    print(i)

def check(num: float)-> None:##num is a parameter
    if num<= 50.0:
        print("Has not Passed")
    else:
      print("Has Passed")
    return

def check_two(num: float)-> bool:
    if num<= 50.0:
        return True
    else:
        return False
def calculate_area(radius:float)-> float:
    return 3.14*(radius**2)##efficiency
    # PI:float=3.14
    # radius_square: float=radius*radius
    # return PI*radius_square
print(calculate_area(7.2))

def calculate_sum(a:float,b:float)->float:
    return a+b

def calculate_sum_ii(a:float,b:float)->float:
    return a+b

def calculate_sum_iii(a:float,b:float)->float:
    return a+b







# check(89.9)##89.9 is an argument(the actual value)
# check_two(45.7)
#
# has_passed: bool=check_two(30.2)
# print(has_passed)