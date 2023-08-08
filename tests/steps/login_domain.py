class LoginDomain(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        return 'user is on the login page'
    
    def enter_credentials(self):
        return f'Entered username: {self.username}, password {self.password}'
        
    def login_button(self):
        pass
        
    def correct_login_details(self):
        if self.username == 'correct_user' and self.password == 'correct_passowrd123@':
            return 'user successfully logs in and redirected to their profile page'

    def incorrect_login_details(self):
        if self.username == 'incorrect_user' and self.password == 'wrong_passowrd123@':
            return 'popup error message is displayed'