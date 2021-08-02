from credential import Credentials
from user import User
import unittest # Importing the unittest module
class TestCredential(unittest.TestCase):

    def setUp(self):
          
        
            self.new_credentials = Credentials('Facebook', 'kelvinrono', '12345')
    def test_init(self):

            '''
            This is a test that confirm that the objects 
            in the credentials cass have been initialized properly
            '''
            self.assertEqual(self.new_credentials.credentials_account, "Facebook")
            self.assertEqual(self.new_credentials.credentials_username, "kelvinrono")
            self.assertEqual(self.new_credentials.credentials_password, "12345")
    
  
      
    def test_save_credentials(self):
            '''
            This is a test than run and check if the contact has been 
            actually saved
            '''
            self.new_credentials.save_credentials()
            self.assertEqual(len(Credentials.credential_details), 1)

    def test_display_all_accounts(self):
        self.assertEqual(Credentials.display_credentials(), Credentials.credential_details)

    def tearDown(self):
        Credentials.credential_details = []

    def test_delete_credential(self):
            """
            test method to test if we can remove an account credentials from our credentials_list
            """
            self.new_credentials.save_credentials()
            test_credentials = Credentials('Twitter','djchep','12343')
            test_credentials.save_credentials()
            
            
            self.new_credentials.delete_credentials()
            self.assertEqual(len(Credentials.credential_details),1)

    def test_find_credential(self):
        """
        test to check if we can find a credential entry by user name and display the details of the credential
        """
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials('test','test','test')
        test_credentials.save_credentials()
        the_credential = Credentials.find_by_username("test")
        self.assertEqual(the_credential.credentials_username,test_credentials.credentials_username)


if __name__ == '__main__':
    unittest.main()