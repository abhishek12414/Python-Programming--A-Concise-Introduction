#%%
def problem1_7():
    #pass # replace this pass (a do-nothing) statement with your code
    b1 = float(input("Enter the length of one of the bases: "))
    b2 = float(input("Enter the length of the other base: "))
    h = float(input("Enter the height: "))
    a = (1/2) * (b1 + b2) * h
    print("The area of a trapezoid with bases", b1, "and", b2, "and height", h, "is", a)