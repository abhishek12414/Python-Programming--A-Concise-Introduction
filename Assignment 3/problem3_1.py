#%%
def problem3_1(txtfilename):
    #pass # replace this pass (a do-nothing) statement with your code
    f = open(txtfilename)
    l = 0
    for line in f:
        print(line,end="")
        l = l + len(line)
    print("\n\nThere are", l, "letters in the file.")