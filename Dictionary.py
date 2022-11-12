print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("***************** BSCOE 2 -2 *******************")
print("********** ASSIGNMENT (DICTIONARY) ****************")

# This is the Dictionary to store the Contacts
ContactDictionary = {}

# Shows the Menu of the Program
print("""\n
        =============== HELLO WELCOME ===============
        -------------- CONTACT TRACING --------------
        \n          MENU
        1 -> ADD AN ITEM         [1]
        2 -> SEARCH              [2]
        3 -> EXIT                [3]
        =============================================
        ---------------------------------------------
        """)

# This will loop the whole program in what the user wants in 1-3 options
while True:
    choices = int(input("what do you want to do? : "))

    if choices == 1:
        Firstname = (input("Enter your First Name: "))
        Lastname = (input("Enter your Last Name: "))
        UsersAddress = (input("Enter your Address Location: "))
        PhoneNumber = (input("Enter your Contact Number: "))
        Gender = (input("Enter your Gender: "))
        print("\nYou have Successfully added a new Contact for Contract Tracing")



