from Rubrica import Rubrica


while True:
    print('''
    custom                  ___                                             
                           (   )                  .-.                       
     ___ .-.     ___  ___   | |.-.    ___ .-.    ( __)   .--.      .---.    
    (   )   \   (   )(   )  | /   \  (   )   \   (''")  /    \    / .-, \   
     | ' .-. ;   | |  | |   |  .-. |  | ' .-. ;   | |  |  .-. ;  (__) ; |   
     |  / (___)  | |  | |   | |  | |  |  / (___)  | |  |  |(___)   .'`  |   
     | |         | |  | |   | |  | |  | |         | |  |  |       / .'| |   
     | |         | |  | |   | |  | |  | |         | |  |  | ___  | /  | |   
     | |         | |  ; '   | '  | |  | |         | |  |  '(   ) ; |  ; |   
     | |         ' `-'  /   ' `-' ;   | |         | |  '  `-' |  ' `-'  |   
    (___)         '.__.'     `.__.   (___)       (___)  `.__,'   `.__.'_.   
                                                made by github.com/nestyk              
    
    ''')

    print('''
    [1] - Create Contact
    [2] - Call Contact
    [3] - Show Contacts
    [4] - Search Contact
    [5] - Edit Contact
    [6] - Delete Contact
    [7] - Exit
    ''')
    c = int(input("Insert your Choice: "))
    rb = Rubrica()
    if c == 1:
        rb.createContact()
    elif c == 2:
        rb.callContact()
    elif c == 3:
        rb.showContacts()
    elif c == 4:
        rb.searchContact()
    elif c == 5:
        rb.editContact()
    elif c == 6:
        rb.deleteContact()
    elif c == 7:
        print("[!] EXITING")
        print("have a good day!")
        break
    else:
        print("[!] Choice not recognized. Make sure you've wrote the right number.")
        print("[!] EXITING")
