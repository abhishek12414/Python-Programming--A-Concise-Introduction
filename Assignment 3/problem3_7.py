#%%
def problem3_7(csv_pricefile, flower):
    #pass # replace this pass (a do-nothing) statement with your code
    import csv
    f = open(csv_pricefile)
    for i in csv.reader(f):
        if i[0] == flower:
            print(i[1])