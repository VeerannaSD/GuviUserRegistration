import re
import os
'''Login using proer username and password. Only authenticated users are allowed'''
'''Register with valid format ser and password'''
'''Use forgot password feature incase you forget credentials'''
username_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validate_username(user_name):
    '''username validation format username@handler.domain'''
    
    if(re.fullmatch(username_regex, user_name)):
        return True
    else:
        return False


def create_user_dictionary():
    '''Creating dictionary of users and respective passwords from file'''
    user_dictionory={}
    try:
        cwd = os.getcwd()
        
        file1 = open(cwd+"\Registered_Users.txt", 'r')
        Lines = file1.readlines()
        for line in Lines:
            key,value=line.split(':')
            user_dictionory[key]=value.strip()

    except:
        print('Exception in file handling...')
    return user_dictionory


def password_validation(password):
    '''password must have 
                    minimum of 1 special char,
                    minimum of 1 uppercase 
                    minimum of 1 lower case 
                    minimum of 1 digit and 
                    password length between 5-16'''
    
    special_chars=['$', '@', '#', '%']
    
    flag=True
    
    if len(password)<6:
        print('Password lenght is too small Length shold between 5 to 16')
        flag=False
    
    if len(password)>15:
        print('Password length is to large Length should be bewteen 5 to 16')
        flag=False
    
    if not any(char.isdigit() for char in password):
        print('Password must have at least one digit')
        flag=False
    
    if not any(char.isupper() for char in password):
        print('Passowrd must have atleast one upper case letter')
        flag=False
    
    if not any(char.islower() for char in password):
        print('Passowrd must have atleast one Lower case letter')
        flag=False

    if not any(char in special_chars for char in password):
        print('Password must have atleast one special character $,@,#,%')
        flag=False

    if flag:

        return flag
    else:
        return flag

def register_user():
    '''==========Register functionality=========='''
    user_name=input('Enter user name in format (username@handler.domain): ')
    user_password = input('Enter strong passowrd: password must have min 1 special char,min 1 uppercase 1 lower case 1 digit and length between 5-16: ')
    username_validation=validate_username(user_name)
    
    password_validate=password_validation(user_password)
    
    if username_validation and password_validate:
        valid_registering_user = user_name+':'+user_password+'\n'
        try:
            cwd = os.getcwd()
            
            registered_users_file = open(cwd+"\Registered_Users.txt", "a+")

            registered_users_file.write(valid_registering_user)
            registered_users_file.close()

            print(f'User {user_name} registered succefully..')
        except:
            print('Exception in File handling')
    else:
        print('Enter correct username and password')


def login_user():
    '''==========login functionality=========='''
    '''Get all users in Dictionary , validate username and password , Check credentials of user by getting data from file'''

    dicts_users = create_user_dictionary()
    usernames=dicts_users.keys()
    passwords = dicts_users.values()
    
    '''Get username and password from user'''
    user_name = input('Enter user name in format (username@handler.domain): ')
    user_password = input('Enter strong passowrd: password must have min 1 special char,min 1 uppercase 1 lower case 1 digit and length between 5-16: ')
    
    '''Valid entered username and password'''
    username_validation=validate_username(user_name)
    password_validate=password_validation(user_password)
    
    if username_validation and password_validate:
        print('Entered credentials are validated...')
        if user_name in usernames and dicts_users[user_name]==user_password:
            print('User is authenticated....and is valid user \n Logged in successfully..')
        else:
            print('Entered Credentials are not matching..Please login again \n If You are New User Please register before Login')
    else:
        print('Username or password is not valid')




def forgot_password():
    '''==========forgot passowrd=========='''

    dicts_users = create_user_dictionary()
    usernames=dicts_users.keys()
    passwords = dicts_users.values()
    user_name = input('Enter user name in format (username@handler.domain): ')
    username_validation=validate_username(user_name)
    if username_validation:
        if user_name in usernames:
            print(f'Login using {user_name} and {dicts_users[user_name]}')
        else:
            print(f'Entered user {user_name} is not Registered...Please register user and Login')
    else:
        print('Enter user in correct format:(username@handler.domain)')



def main():
    '''Main method Choose list of options for user'''
    while True:
        print("Press your choices:\n1--->Login\n2--->Register\n3--->Forgot Passowrd\n4--->Exit")
        try:
            user_input=int(input())
            if user_input==1:
                login_user()
            elif user_input==2:
                register_user()
            elif user_input==3:
                forgot_password()
            elif user_input==4:
                break
            else:
                print("Please select below choices only:\n1--->Login\n2--->Register\n3--->Forgot Passowrd")
        except:
            print("Enter valid choice")
            print("Please select below choices only:\n1--->Login\n2--->Register\n3--->Forgot Passowrd")

if __name__=="__main__":
    '''Driver code'''
    main()