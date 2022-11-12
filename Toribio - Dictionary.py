print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("***************** BSCOE 2 -2 *******************")
print("********** ASSIGNMENT (DICTIONARY) ****************")

# This is the Dictionary to store the Contacts
ContactDictionary = {}


# Shows the Menu of the Program
def print_menu():
    print("""\n
        =============== HELLO WELCOME ===============
        -------------- CONTACT TRACING --------------\n
                            MENU
                 1 -> ADD AN ITEM         [1]
                 2 -> SEARCH              [2]
                 3 -> EXIT                [3]\n
        =============================================
        ---------------------------------------------
        """)


print_menu()

# This will loop the whole program in what the user wants in 1-3 options
while True:
    option = int(input("\nHi! Please Choose an option on what do you want to do? (From 1-3) : "))

# This is the option 1 that will enter the infos of the user
    if option == 1:
        print("\n=========== ADD Information =============")
        Fullname = (input("\nPlease Enter your Full Name: "))
        UsersAddress = (input("Enter your Address Location: "))
        PhoneNumber = (input("Enter your Contact Number: "))
        Gender = (input("Enter your Gender: "))
        Occupation = (input("Enter your occupation: "))
        Age = (int(input("Enter your age: ")))

        ContactDictionary[Fullname] = {"Full Name": Fullname, "Address": UsersAddress,
                                       "Phone Number": PhoneNumber, "Gender": Gender,
                                       "Occupation": Occupation,
                                       "Age": Age}
        print("\n===== THIS IS THE ENTERED INFORMATION =====")
        print("\nThis is the entered Fullname:", Fullname)
        print("This is the entered Address:", UsersAddress)
        print("This is the entered Phone Number:", PhoneNumber)
        print("This is the entered Gender:", Gender)
        print("This is the entered Occupation:", Occupation)
        print("This is the entered Age:", Age)
        print("\nYou have Successfully added a new Contact for Contact Tracing")
        print_menu()

    # This is the option 2, that will search a users full name in the Dictionary
    elif option == 2:
        print("\n============== SEARCH CONTACTS =============")
        Fullname = (input("\nPlease input the full name of the person that you want to search: "))

        if Fullname in ContactDictionary.keys():
            for Contacts in ContactDictionary[Fullname].items():
                print("This is the information found in the Dictionary of: ", Contacts[0], ":", Contacts[1])
            print("\nYou have Successfully Searched a Contact in the Dictionary")
        else:
            print("\nThe entered Full name is not found in the Dictionary")
            print_menu()

    # This is option 3, that will exit the program
    elif option == 3:
        print("============== EXIT THE PROGRAM =============")
        ExitOrRetry = input("Do you want to exit or retry: (yes")
        if ExitOrRetry == "yes":

            print("""\n
            =====================================================
            -----------------------------------------------------
            || Thank you for using the Contact Tracing Program ||
            ||                                                 ||
            ||                   Goodbye!                      ||
            =====================================================
            """)

            break

        else:
            print("\nRetry the Program, Go Back to Main Menu")
            print_menu()

    # Unknown Option of Menu
    else:
        print("\nSorry but", option, "is not a valid option")
        print("Try Again!")
        print_menu()
