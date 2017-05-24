#%%
def problem4_1(wordlist):
    """ Takes a word list prints it, sorts it, and prints the sorted list """
    #pass # replace this pass (a do-nothing) statement with your code
    print(wordlist)
    wordlist.sort(key=str.lower)
    print(wordlist)