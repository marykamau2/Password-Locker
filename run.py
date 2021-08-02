#!/usr/bin/env python3.8
from user import User
import random
from credential import Credentials
def createUserAccount(firstName, lastName, username, password):
    '''
    This function will create a new user account
    '''
    new_user = User(firstName, lastName, username,password)
    return new_user

def create_credentials(credential_account, credential_username,credential_password):
    '''
    Function to create new contact
    '''
    new_credentials = Credentials(credential_account, credential_username, credential_password)
    return new_credentials


def save_user(user):
    '''
    Function that will save the user
    '''


def save_credentials(credential):
    '''
    Function to save contact
    '''
    credential.save_credentials()

def delete_credentials(credential):
    '''
    This is a function that deletes credentials
    '''
    Credentials.delete_credentials()
def display_user():
    return User.display_user()
def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_by_username(account)

def display_credentials():
    return Credentials.display_credentials()

def randomgenerator():
    '''
    This is a method that will create random passwords
    '''
    rand = random.randint(10000,99999)
    return rand

def main():
    print('Welcome to password Locker app,please enter your name \n ')
    user_name = input()
    print(f"Hello {user_name}, ")
    print("\n")

    while True:
        print(" You will need to create an Password Locker account first before you start saving your credentials! \nProceed using these short code. \n na - create a new Locker,\n  ex - exit the password locker app")
        short_code = input().lower()

        if short_code == 'na':
            print("New Password Locker Account")
            print("-"*30)
            
            print("Enter your username : ")
            userName = input()
            
            print("Enter your first name : ")
            first_name = input()

            print("Enter the last name : ")
            last_name = input()

            print("Enter your password : ")
            password = input()

            save_user(createUserAccount(first_name, last_name, userName,password))#create and save new contact
            print("\n")
            print(f"Congratulations! {first_name} {last_name}, You have created password locker account. Proceed to store you credentials now.\n")
            print("\n")

            while True:
                print("Use these short codes:\n add - Add credentials details,\ndc - display stored credential details,\nex - exit the contact list, \n del - delete account")
                short_code = input().lower()
                
                if short_code == 'add':
                    print("New Credentials account")
                    print("-"*30)
                    
                    print("Account Type(eg. Facebook, twitter, instagram...) : ")
                    type = input()
                    
                    print("User name : ")
                    username = input().lower()
                    while True:
                        print("use these codes to choose the password modes:\n gp - system generated password,\n tp - type password,\n ")
                        pass_code = input().lower()
                        enteredPassword = ''
                        if pass_code=='tp':
                            print('Enter your password')
                            enteredPassword = input()
                        elif pass_code=='gp':
                            print('Enter your password')
                            enteredPassword = randomgenerator()

                        save_credentials(create_credentials(type, username, enteredPassword))#create and save new contact
                        print("\n")
                        print(f"New credentials details for account {type} saved successfully. \n Username: {username} \n password is: {enteredPassword}")
                        print("\n")

                        break
                elif short_code == 'dc':

                    if display_credentials():
                        print("These are the accounts saved in the app: \n ")
                        print('\n')

                        for credential in display_credentials():
                                print(f" Account type:{credential.credentials_account} \n Username: {credential.credentials_username} \n Password: {credential.credentials_password}")

                        print('\n')

                    else:
                        print('There is no credentials saved')

                elif short_code == "del":
                    print("Enter Username of the Credentials you want to delete")
                    search_name = input().lower()
                    if find_credential(search_name):
                        search_credential = find_credential(search_name)
                        print("_"*40)
                        search_credential.delete_credentials()
                        print('\n')
                        print(f"Your stored credentials for : {search_credential.credentials_username} successfully deleted!!!")
                        print('\n')
                    else:
                        print(" \n The Credential you want to delete does not exist \n")
                            
                    pass
                elif short_code =='ex':
                        print('\n')
                        print("Thanks for using the app. Welcome")
                        break
          
        break
      

        

main()