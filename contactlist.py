contacts = {}

while True:

	inp = raw_input("""Enter s to search in list\nor type a to add to the list \nor p to print the complete list\nor x to exit  """)

	if inp.lower() == 'x':
		break
	elif inp.lower() == "p":
		print contacts.items()
	elif inp.lower() == 's':
		find = raw_input("Enter the name to search:  ")
		if find in contacts.keys():
			print contacts[find]
		else:
			print ("Not found Type a to add new contact:  ")
	elif inp.lower() == 'a':
		newname = raw_input("Enter new name:  ")
		newcontact = raw_input("Enter contact number:  ")
		contacts[str(newname)] = newcontact
