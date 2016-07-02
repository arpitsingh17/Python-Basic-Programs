#list to hold new items
shopping_list = []
#message prompt for the user


def show_help():
    print("TYPE DONE to exit\n"
          "Type SHOW to see the current items\n"
          "Type DONE to exit adding and see the items\n")
def print_list():
    print("\n\nHere's your list")
    for new_item in shopping_list:
        print(new_item)
    print("you have {} items".format(len(shopping_list)))
print("Enter new item to add")
show_help()
while True:
    new_item = input("> ")
# check for done
    if (new_item == "DONE"):
        break
    elif (new_item=="SHOW"):
        print_list()
    elif (new_item=="HELP"):
        show_help()
        continue
#add new item to the list
    shopping_list.append(new_item)

print_list()
