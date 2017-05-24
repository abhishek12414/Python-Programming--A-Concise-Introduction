#%%
def problem3_3(month, day, year):
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
    #pass # replace this pass (a do-nothing) statement with your code
    mon = ""
    if(month == 1):
        mon = "January"
    elif(month == 2):
        mon = "Febuary"
    elif(month == 3):
        mon = "March"
    elif(month == 4):
        mon = "April"
    elif(month == 5):
        mon = "May"
    elif(month == 6):
        mon = "June"
    elif(month == 7):
        mon = "July"
    elif(month == 8):
        mon = "August"
    elif(month == 9):
        mon = "September"
    elif(month == 10):
        mon = "October"
    elif(month == 11):
        mon = "November"
    elif(month == 12):
        mon = "December"
    
    #June 17, 2016
    s = mon + " " + str(day) + ", " + str(year)
    print(s)