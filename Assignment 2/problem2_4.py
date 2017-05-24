#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    #pass # replace this pass (a do-nothing) statement with your code
    li = []
    for i in range(10):
        #print(random.randint(0,5), "  ", random.randint(30,35))
        li.append(random.random() * 5 + 30)
    print(li)
