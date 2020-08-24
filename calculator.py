def interface():
    print("My Program")
    while True:
        print("Options")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
            
def HDL_driver():
    # Get input
    entered_HDL = get_input()
    # Check if HDL is normal
    # Output

def get_input():
    userHDL = input("Please enter your HDL: ")
    return int(userHDL)



interface()

