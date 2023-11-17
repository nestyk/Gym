import json
import os.path


class Rubrica:

    def __init__(self):
        # check if path exists
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as f:
                self.contactsJson = json.load(f)
        else:
            self.contactsJson = {}
            with open("contacts.json", "w") as f:
                pass

    def updateFile(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contactsJson, f)

    def getContactsID(self):
        contactsID = []
        for a in self.contactsJson:
            contactsID.append(a)
        return contactsID

    def createContact(self):

        newID = int(self.getContactsID()[-1]) + 1  # aggiunge 1 all'ultimo ID; esempio: ultimo id è 2, ID=3
        name = input("Insert Contact Name: ")
        surname = input("Insert Contact SurName: ")
        number = input("Insert Contact Number: ")
        if not number.startswith("+39"):
            number = "+39" + number
        email = input("Insert Email: ")

        self.contactsJson[newID] = {
            "name": name,
            "surname": surname,
            "phoneNumber": number,
            "email": email
        }
        # print(self.contactsJson) DEBUG
        self.updateFile()
        print("Done")

    def callContact(self):
        number = input("Insert Phone Number to call: ")
        for a in self.contactsJson:
            if number in self.contactsJson[a]["phoneNumber"]:
                print("I'm calling " + self.contactsJson[a]["name"] + " " + self.contactsJson[a]["surname"])
                print("Phone Number: " + self.contactsJson[a]["phoneNumber"])
            else:
                print("Contact not found. Do you want to Create it? y/n")
                c = input()
                if c.lower() == "y":
                    self.createContact()
                    break
                elif c.lower() == "n":
                    pass
                else:
                    print("Choice not recognized.")

    def showContacts(self):
        print("\t\tLISTA CONTATTI:")
        for a in self.contactsJson:
            print(" - " + a)
            print(" \tNome Contatto: " + self.contactsJson[a]["name"])
            print(" \tCognome Contatto: " + self.contactsJson[a]["surname"])
            print(" \tNumero Contatto: " + self.contactsJson[a]["phoneNumber"])
            print(" \tEmail Contatto: " + self.contactsJson[a]["email"])

    def searchContact(self):
        number = input("Insert Phone Number to search: ")
        for a in self.contactsJson:
            if number in self.contactsJson[a]["phoneNumber"]:
                print("Name: " + self.contactsJson[a]["name"] + " Surname: " + self.contactsJson[a]["surname"])
                print("Phone Number: " + self.contactsJson[a]["phoneNumber"])
            else:
                print("Contact not found. Do you want to Create it? y/n")
                c = input()
                if c.lower() == "y":
                    self.createContact()
                    break
                elif c.lower() == "n":
                    pass
                else:
                    print("Choice not recognized.")

    def editContact(self):
        self.showContacts()
        ID = int(input("Insert Contact ID: "))
        for id in self.getContactsID():

            if ID == int(id):
                c = int(input('''What do you want to edit? 
                1 - Name
                2 - Surname
                3 - Number
                4 - Email
                '''))
                if c == 1:
                    name = input("Insert new Name: ")
                    self.contactsJson[id]["name"] = name
                elif c == 2:
                    surname = input("Insert new SurName: ")
                    self.contactsJson[id]["surname"] = surname
                elif c == 3:
                    number = input("Insert new number: ")
                    self.contactsJson[id]["phoneNumber"] = number
                elif c == 4:
                    email = input("Insert new email: ")
                    self.contactsJson[id]["email"] = email
                else:
                    print("Choice not recognized.")
                self.updateFile()
                break

    def deleteContact(self):
        self.showContacts()
        ID = input("Insert Contact ID: ")
        if ID in self.getContactsID():
            del self.contactsJson[ID]
            self.updateFile()
        else:
            print("ID Not found.")
