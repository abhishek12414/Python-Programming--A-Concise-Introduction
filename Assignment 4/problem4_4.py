#%%
import csv
import os

phones = []
pheader = ['Name', 'Phone Number']
name_pos = 0
phone_pos = 1

def load_phone_list():
    if os.access("myphones.csv",os.F_OK):
        f = open("myphones.csv")
        for row in csv.reader(f):
            phones.append(row)
        f.close()

def show_phones():
    show_phone(pheader, "")
    index = 1
    for phone in phones:
        show_phone(phone, index)
        index = index + 1
    print()

def show_phone(phone, index):
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print(outputstr.format(index, phone[name_pos], phone[phone_pos]))

def save_phone():
    f = open("myphones.csv", 'w', newline='')
    for item in phones:
        csv.writer(f).writerow(item)
    f.close()

def main_loop():
    load_phone_list()
    while True:
        ch = menu_choice()
        if ch == "None":
            continue
        elif ch == "s":
            show_phones()
        elif ch == "r":
            reorder_phones()
        elif ch == "q":
            break;
    save_phone()

def menu_choice():
    print("   s) Show")
    print("   r) Reorder")
    print("   q) Quit")
    choice = input("Choice : ").lower()
    if choice in ['s', 'r', 'q']:
        return choice
    else:
        print("Invalid")
        return None;
    
def reorder_phones():
    global phones       # this insures that we use the one at the top
    #pass # replace this pass (a do-nothing) statement with your code
    phones.sort()
    
if __name__ == '__main__':
    main_loop()