
#Peter J. Mangelsdorf
#pjm349@drexel.edu
#Dr. William Mongan
#CS 265
#17 March 2019

'''Name:
        FUNCTIONAL Bank Accounts Management System for *Nix Systems
   Description:
        Third Assignment for CS265. Not as bad as the postfix calculator, but pretty steep with handling abstraction of options'''



'''Imports'''
'''Any libraries other people wrote that I need'''

#Needed for accessing the OS log
import os

#Needed for managing the program
import sys

#Needed for Dating the Transactions and Logs
import datetime



'''Program Variables'''
'''Sorry, no tuple or other immutable data types. Those are a little beyond what I wanted to achieve.
Anything which other functions would need to reference is placed here. Totally UN functional and UNcool, I know'''

#Used for internally tracking any regular events as they occur
accounting_events = "Acct Events\n"
menu_events = "Menu Events\n"
file_events = "File Events\n"
control_events = "Ctrl Events\n"

#Used for internally tracking any errors as they occur, without notifying the user or crashing
accounting_errors = "Acct Errs\n"
menu_errors = "Menu Errs\n"
file_errors = "File Errs\n"
control_errors = "Ctrl Errs\n"
argument_errors = "Arg Errs\n"

#Used for consolidating all program information. Anonymously records accounting transactions
system_log = [accounting_events, menu_events, file_events, control_events, accounting_errors, menu_errors, file_errors, control_errors, argument_errors]

#Used for tracking transactions within the application. Is a list of all transactions
my_log = ""

#Used for tracking the FINAL options, which are sorted alphabetically for the user to peruse
#Example: 1 Nancy Magill 1902
#Note the exclusion of a parenthesis. This is added in pretty printing later.
options = {}

#Used for tracking user balances
#Database of account number to account details
#Works as an intermediary between my_log and the final output.
#Example: "8273":"Rocky Raccoon 520.00"
accounts = {}



'''Argument Functions'''
'''For initially deciding how the program should modify its overall behavior'''

#Checks the Arguments for correct usage
def get_args():
    if len(sys.argv) >= 2:
        for argument in sys.argv:
            if argument == "account" or "-i" or "-h" or "-t" or "?":
                pass
            else:
                print("Invalid Arguments Given.")
                stop()
    else:
        print("No Arguments Given.")
        teach_args()
        stop()

#Determines an action based on the user's arguments
def use_args():
    global control_events
    for argument in sys.argv:
        if argument == "account":
            pass
        elif argument == "-i":
            control_events = control_events + "Program startup successful.\n"
            account_info()
        elif argument == "-h":
            control_events = control_events + "Program startup successful.\n"
            account_history()
        elif argument == "-t":
            control_events = control_events + "Program startup successful.\n"
            account_transact()
        elif argument == "-?":
            teach_args()
            stop()
        else:
            global argument_errors
            argument_errors = argument_errors + "Error: use_args with " + argument + " as argument.\n"
            stop()
            
#Demonstrates what args may be used and how to supply them
def teach_args():
    print("account - An account management program for *Nix Systems\n")
    print("USAGE: account -argument\n")
    print("OPTIONS:\n -? Shows this Message\n")
    print(" -h Interactive Mode for Querying History of User Transactions\n")
    print(" -t Interactive Mode for Inserting User Transactions\n")
    print(" -i Interactive Mode for Querying Infomation of User Accounts\n")



'''Menu Functions'''
'''The meat of the program, just handling the abstractions of handling things to be printed to the user'''

#Prints Data relevant to Info Querying
def info_menu():
    global options
    print("   Info   ")
    print("----------")
    show_options()
    print("q) Quit")
    
#Prints minimenu for information results
def info_query(account, name, balance):
    print("Account Number: " + account)
    print("Account Holder: " + name)
    print("Account Balance: " + balance)
    input("[Press Enter to Return to Info]")

#Prints Data relevant to History Querying
def history_menu():
    global options
    print("  History  ")
    print("-----------")
    show_options()
    print("q) Quit")

#Prints the Minimenu for history results
def history_query(number):
    global my_log
    user_history = []
    for line in my_log:
        line_list = line.split(":")
        if line_list[0] == number:
            user_history.append(line)
    #Sort by Year, Sort by Month, Sort by Day
    user_history.sort()
    for entry in user_history:
        print(entry)

#Prints Data relevant to Transaction Insertion
def transact_menu():
    global options
    print("  Transact  ")
    print("------------")
    show_options()
    print("q) Quit")
    
#Prints the minimenu for transaction insertion
def transact_query(number, name):
    global my_log
    print("Transaction:")
    print("w - Withdrawal")
    print("d - Deposit")
    done = False
    while not done:
        action = input("User Action: ").upper
        if action != "w" or "d":
            print("Invalid Transaction. Try again.")
        else:
            done = True
    print("Amount:")
    print("0 - New Account")
    amount = input("User Amount: ")
    date = ".".join(datetime.datetime.now().split(" ")[0].split("-"))
    transaction = number + ":" + name + ":" + date + ":" + action + ":" + amount    
    my_log = my_log + "\n" + transaction

#Pretty Prints the options dictionary, so the dictionary can be handled regularly
def show_options():
    for option in options:
        print(option + ") " + options[option])
    
#Gets and checks the user's input. Must be an integer, quit, or help
def get_option():
    global options
    done = False
    while not done:
        option = input("User Action: ").casefold()
        if option == "?" or "q":
            done = True
        elif option != "?" or "q":
            try:
                int(option) #To test whether option is an integer
                if option in options:
                    done = True
                else:
                    print("Invalid Choice. Please Choose Again.\n")
            except:
                global menu_errors
                menu_errors = menu_errors + "Error: get_option with " + option + " as option.\n"
        else:
            print("Invalid Choice. Please Choose Again.\n")
    return option

#Updates the accounts database dictionary according to my_log
#    list_line =  "8273" : "Rocky Raccoon" : "08.10.17:D" : "520.00"
#    Result: {'8273' : "Rocky Raccoon 520.00"}
#This one is a real monster, beware
def update_accounts():
    global accounts
    global my_log
    for line in my_log:
        line_list = line.split(":")
        for acct_number, data in accounts.items():
            if line_list[0] == acct_number:
                pass
                 
#Updates the FINAL options dictionary according to the incomplete dictionary
#    Result: 1 : Nancy Magill 1902
def update_options():
    global inc_options
    global options
    for option_number, option_data in options.items():
        pass

#Notifies user of legal consequences
def warning():
    warning = "Unauthorized use of this system is a punishable offense\n[Press Enter to Acknowledge Consent]\n[Press CTRL+C to Cancel]\n"
    consent = input(warning)
    if consent == "":
        consent = "blank"
    global control_events
    control_events = control_events + "\nUser consented to legal consequences with " + consent + ".\n"

#Notifies user of program name
def greeting():
    greeting = "Welcome to Fry Banks Accounting Management System\n[Press Enter to Continue]\n[Press CTRL+C to Cancel]\n"
    input(greeting)

#Notifies user of program completion
def goodbye():
    goodbye = "Thank You for Transacting with Fry Banks"
    print(goodbye)



'''Accounting Functions'''
'''The heart of the program - Each is a unique mode of interaction with the data.'''

#Determines an action based on the user's input for information querying
def account_info():
    global options
    global accounting_events
    global accounts
    update_accounts()
    update_options()
    done = False
    while not done:
        info_menu()
        option = get_option()
        if option == "q":
            accounting_events = accounting_events + "User Quit Info Querying\n"
            done = True
        else:
            #If an option is an account, we need to get the relevant info from that account and send it to the actual action to handle it.
            number = options[option].split(" ")[-1]
            name = " ".join(options[option].split(" ")[:1])
            balance = accounts[number].split(" ")[-1]
            info_query(number, name, balance)
            accounting_events = accounting_events + "User Queried Information\n"

#Determines an action based on the user's input for history querying
def account_history():
    global options
    global accounting_events
    global accounts
    update_accounts()
    update_options()
    done = False
    while not done:
        history_menu()
        option = get_option()
        if option == "q":
            accounting_events = accounting_events + "User Quit History Querying\n"
            done = True
        else:
            #If an option is an account, we need to get the relevant info from that account and send it to the actual action to handle it.
            accounting_events = accounting_events + "User Queried History\n"

#Determines an action based on the user's input for transaction insertion
def account_transact():
    global options
    global accounting_events
    global accounts
    update_accounts()
    update_options()
    done = False
    while not done:
        transact_menu()
        option = get_option()
        if option == "q":
            accounting_events = accounting_events + "User Quit Transaction Insertion\n"
            done = True
        else:
            #If an option is an account, we need to get the relevant info from that account and send it to the actual action to handle it.
            number = options[option].split(" ")[-1]
            name = " ".join(options[option].split(" ")[:1])
            transact_query(number, name)
            #Because this is an effect on a datastructure, we must update all other structures to this change.
            update_logs(compare_logs())
            accounting_events = accounting_events + "User Inserted Transaction\n"



'''File Functions'''
'''Anything to do with input or output, or anything at all with the OS, is done here'''

#Updates the internal log based on the OS's log
def update_my_log():
    if "ACCT_LIST" in os.environ:
        for line in os.environ["ACCT_LIST"]:
            if line in my_log:
                pass
            else:
                my_log.append(line)
        global file_events
        file_events = file_events + "Updated MY log.\n"
    else:
        global file_errors
        file_errors = file_errors + "Error: update_my_log with " + os.environ["ACCT_LIST"] + " as OS log.\n"

#Updates the OS's log based on the internal log
def update_os_log():
    if "ACCT_LIST" in os.environ:
        for line in my_log:
            if line in os.environ["ACCT_LIST"]:
                pass
            else:
                os.environ["ACCT_LIST"] = os.environ["ACCT_LIST"] + "\n" + line
        global file_events
        file_events = file_events + "Updated OS log.\n"
    else:
        global file_errors
        file_errors = file_errors + "Error: update_os_log with " + my_log + " as MY log.\n"

#Compares differences between logs and returns the most up to date log
def compare_logs():
    global my_log
    if "ACCT_LIST" in os.environ:
        os_length = len(os.environ["ACCT_LIST"])
    else:
        os_length = 0
    target = ""
    if len(my_log) > os_length:
        target = "os"
    elif len(my_log) < os_length:
        target = "my"
    else:
        target = "none"
    return target

#Calls the appropriate updater depending on which log must be updated
def update_logs(log):
    if log == "my":
        update_my_log()
    elif log == "os":
        update_os_log()
    elif log == "none":
        pass
    else:
        global file_errors
        file_errors = file_errors + "Error: update_logs with " + log + " as target log.\n"

#Updates the system log. Use to refresh, in event of program lag
def update_system_log():
    global system_log
    system_log = [accounting_events, menu_events, file_events, control_events, accounting_errors, menu_errors, file_errors, control_errors, argument_errors]

#Shows all events during program uptime
def show_system_log():
    global system_log
    for category in system_log:
        print(category)

#Saves system log to Disk
def save_system_log():
    global system_log
    with open('account.system.log', 'a') as log_file:
        for category in system_log:
            log_file.write(category)



'''Control Functions'''
'''Anything which controls the flow of the overall program is placed here'''
'''Initially, I tried making this entirely Functional instead of Procedural, cried, and gave up'''

#Saves all data and quits
def stop():
    update_logs(compare_logs())
    update_system_log()
    save_system_log()
    goodbye()
    sys.exit()

#Loads all data and kicks the program into operation
def start():
    update_logs(compare_logs())
    update_accounts()
    update_options()
    greeting()
    warning()
    get_args()
    use_args()

#Manages the program. Literally just calls other functions.
def main():
    start()
    stop()

#For modularity, this is the only procedural script.
if __name__ == '__main__':
    main()
