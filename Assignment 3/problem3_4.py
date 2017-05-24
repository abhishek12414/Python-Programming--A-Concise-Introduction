#%%
def problem3_4(mon, day, year):
    """ Takes date such as July 17, 2016 and write it as 7/17/2016 """
    #pass # replace this pass (a do-nothing) statement with your code
    m  = 0
    if(mon == "January"):
        m = 1
    elif(mon == "Febuary"):
        m = 2
    elif(mon == "March"):
        m = 3
    elif(mon == "April"):
        m = 4
    elif(mon == "May"):
        m = 5
    elif(mon == "June"):
        m = 6
    elif(mon == "July"):
        m = 7
    elif(mon == "August"):
        m = 8
    elif(mon == "September"):
        m = 9
    elif(mon == "October"):
        m = 10
    elif(mon == "November"):
        m = 11
    elif(mon == "December"):
        m = 12

    #7/17/2016
    s = str(m) + "/" + str(day) + "/" + str(year)
    print(s)