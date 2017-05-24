#%%
def problem2_8(temp_list):
    #pass # replace this pass (a do-nothing) statement with your code
    sum = 0
    m = max(temp_list)
    n = min(temp_list)
    for i in temp_list:
        sum += i
    avg = sum / len(temp_list)
    print("Average:", avg)
    print("High:", m)
    print("Low:", n)