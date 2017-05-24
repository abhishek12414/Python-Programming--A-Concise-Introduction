#%%
def problem4_3(product, cost):
    """ Prints the product name in a space of 25 characters, left-justified
        and the price in a space of 6 characters, right-justified"""
    #pass # replace this pass (a do-nothing) statement with your code
    #print("toothbrush               $  2.60")
    print("{0:25}${1:6.2f}" .format(product, cost) )