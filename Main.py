import getpass




class Password_Manager:
    def __init__(self):
        self.user = None
        self.password = None
        self.file_name = None 
        self.history = {}

    def accept_password(self):

        try:

            while True:
                username = input("Enter a name for this password: ")
                if username == "":
                    print("Username canot be empty!")
                else:
                    break

            while True:
                # FOR HIDDING PASWORD GONNA ACTIVATE THIS LATER
                # passw = getpass.getpass("Please enter your password: ")
                
                passw = input("Please enter your password: ")                               
                if passw == "":
                    print("Password canot be empty!")
                else:
                    break

            self.history[username] = passw
                
        except Exception as e:
            print(f"Error: {e}")





            


if __name__ == "__main__":

    pm = Password_Manager()
    pm.accept_password()