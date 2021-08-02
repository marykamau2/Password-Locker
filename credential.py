class Credentials:
    
    credential_details = [] #initialize an array to store the credential details
     def __init__(self,credentials_account, credentials_username, credentials_password):
        '''
        This will initialize the credentials details required for the credentials class
        '''
        self.credentials_account = credentials_account
        self.credentials_username = credentials_username
        self.credentials_password = credentials_password
     def save_credentials(self):
         '''
         Save the credentials of a user
         '''
         Credentials.credential_details.append(self)
