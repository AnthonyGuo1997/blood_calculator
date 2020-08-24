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
    compared_result = check_HDL(entered_HDL)
    # Output
    give_output(entered_HDL, compared_result)

def get_input():
    userHDL = input("Please enter your HDL: ")
    return int(userHDL)

def check_HDL(entered_HDL):
    if entered_HDL >= 60:
        return "Normal"
    elif 40 <= entered_HDL < 60:
        return "Borderline Low"
    else:
        return "Low"

def give_output(entered_HDL, compared_result):
    print("Your HDL value is {}".format(entered_HDL))
    print("Comparing to the standards, your HDL is {}".format(compared_result))
    return


interface()

