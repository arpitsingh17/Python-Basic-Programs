#list to hold new items
shopping_list = []
#message prompt for the user
print("Enter new item to add")
print("Enter DONE to finish")
while True:
    new_item = input("> ")
# check for done
    if (new_item == "DONE"):
        break
    elif (new_item=="SHOW"):
        for new_item in shopping_list:
            print(new_item)
    elif (new_item=="HELP"):
        print("TYPE DONE to exit\n"
              "Type SHOW to see the current items\n"
              "Type DONE to exit adding and see the items\n")
        continue
#add new item to the list
    shopping_list.append(new_item)

print("\n\nHere's your list")
for new_item in shopping_list:
    print(new_item)
