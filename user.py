class User:
    user_list = []# Array to store the users accounts
    def __init__(self, firstName, lastName, username):
        '''
        This is used to initialize the properties of the class credentials
        firstName --> initialize the first name of the user
        lastName --> initialize the last name of the user
        user --> initialize the user name of the user
        '''
        self.firstName = firstName
        self.lastName = lastName
        self.username = username


    def save_user(self):
        '''Method to save the detais of a user
        '''
        User.user_list.append(self)
    

    @classmethod
    def display_user(cls):
        return cls.user_list   