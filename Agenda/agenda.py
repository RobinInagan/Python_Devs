import os

class book():

    def __init__(self):
        self.contactos = []

    def addContacts(self):
        os.system('cls')
        print('\nAdding new contact...\n')
        name = input('\nPlease enter the name of the contact\n-->  name = ')
        phone = int(input('\nPlease enter the number of the contact\n-->  phone = '))
        email = input('\nPlease enter the email address of the contact\n-->  email = ')

        self.contactos.append({'name': name, 'phone': phone, 'email': email})

    def listContacts(self):
        os.system('cls')
        print('\nShowing the Contacts...\n')
        if(len(self.contactos) == 0):
            print('\nNo contacts found\n')
        else:
            i=1
            for x in range(len(self.contactos)):
                print('contact {} : Name = {}  Phone = {} Email = {} \n'.format(i,self.contactos[x]['name'],self.contactos[x]['phone'],self.contactos[x]['email']))
                i+=1

        os.system('pause')

    def search(self):
        os.system('cls')
        print('\Searching for a contact:\n')

        name = input('\nPlease enter the name of the contact for which you want to search')

        if(len(self.contactos) == 0):            
            print('\nNo contacts found\n')
        else:
            for x in range(len(self.contactos)):
                if (name == self.contactos[x]['name']):
                    print('\n¡ Contact Found !...\n')
                    print(f"\nName: {self.contactos[x]['name']} Phone: {self.contactos[x]['phone']} Email: {self.contactos[x]['email']} \n")    
    
    def EditContact(self):
        os.system('cls')
        print('\nEditing a contact...\n')

        name = input('\nPlease enter the name of the contact for which you want to search')

        if(len(self.contactos) == 0):            
            print('\nNo contacts found\n')
            os.system('pause')
        else:
            for x in range(len(self.contactos)):
                if (name == self.contactos[x]['name']):
                    print('\n¡ Contact Found !...\n')
                    new_name = input('\nPlease enter the new name of the contact \n ---> name = ')
                    new_phone =  int(input('\nPlease enter the new phone of the contact \n ---> phone = '))
                    new_email = input('\nPlease enter the new mail of the contact \n ---> email = ')

                    self.contactos[x]['name'] = new_name
                    self.contactos[x]['phone'] = new_phone
                    self.contactos[x]['email'] = new_email

                    os.system('pause')



book1 = book()

book1.addContacts()
book1.addContacts()

book1.listContacts()

book1.EditContact()

book1.listContacts()