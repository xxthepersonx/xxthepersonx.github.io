import browser

def start_main_menu():
    print("Address book search!\n\n")
    print("Choose an option:\n")
    print("1) First Name")
    print("2) Last Name")
    print("3) City")
    print("4) State (abbreviation)")
    print("5) Exit")
    choose_main_menu()

def choose_main_menu():
    choice = int(browser.prompt("enter your choice: "))
    if choice == 1:
        search_for_something(choice, "first name")
    elif choice == 2:
        search_for_something(choice, "last name")
    elif choice == 3:
        search_for_something(choice, "city")
    elif choice == 4:
        search_for_something(choice, "state")
    elif choice == 5:
        quit()

def open_file():
    open_file = open("addressBook.csv", "r")
    for each_line in open_file:
        addresses.append(each_line.split(","))

def search_for_something(category, search_term):
	column = 0
	if category == 1:
		column = 0
	elif category == 2:
		column = 1
	elif category == 3:
		column = 3
	elif category == 4:
		column = 4
	query = input(browser.prompt("Enter a %s: " %search_term))
	for x in range(len(addresses)):
	    if addresses[x][column] == query:
	        found_addresses.append(addresses[x])
	list_results()

def list_results():
	browser.alert("\nResults found:", len(found_addresses), "\n")
	if len(found_addresses) > 0:
		for x in range (len(found_addresses)):
            """
			browser.alert("First Name: %s" %found_addresses[x][0])
                            ("Last name: %s" %found_addresses[x][1])
                            ("Street: %s" %found_addresses[x][2])
                            ("City: %s" %found_addresses[x][3])
                            ("State: %s" %found_addresses[x][4])
                            ("Zip Code: %s" %found_addresses[x][5])
                            ("Phone number: %s" %found_addresses[x][6])
                            ("Email: %s" %found_addresses[x][7])
                            """

browser.alert("First Name: %s \
                \nLast name: %s \
                \nStreet: %s \
                \nCity: %s \
                \nState: %s \
                \nZip Code: %s \
                \nPhone number: %s \
                \nEmail: %s" %(found_addresses[x][0], found_addresses[x][1], found_addresses[x][2], found_addresses[x][3], found_addresses[x][4], found_addresses[x][5], found_addresses[x][6])

found_addresses = []
addresses = []
open_file()
start_main_menu()

    
