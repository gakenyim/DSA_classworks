def power(base,exp):
    print("Method Call")
    print("Exp= :",exp)
    print("base= :",base)
    if exp==1:
        print("Base case.No further recursion.No more method calls")
        return base
    if exp!=1:
        print("General case")
        return base*power(base,exp-1)


    base=int(input("Enter the base :"))
    exp=int(input("Enter the exponent :"))
    print("Result: ",power(base,exp))