#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    pass # replace this pass (a do-nothing) statement with your code
    a = float(input("Enter length of side one: "))
    b = float(input("Enter length of side two: "))
    c = float(input("Enter length of side three: "))
    s = .5 * (a + b + c)
    x = s*(s-a)*(s-b)*(s-c)
    x = x**.5
    print("Area of a triangle with sides", a, b, c, "is", x)