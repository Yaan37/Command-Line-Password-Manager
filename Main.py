import getpass
import csv
import os 



class Password_Manager:
    def __init__(self):
        self.account= None
        self.user = None
        self.password = None
        self.file_name = "accounts.csv" 



    def accept_password(self):
        try:

            while True:
                acc = input("Which platform is this username and password for: ")
                if acc == "":
                    print("account name canot be empty!")
                else:
                    break

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

            self.account = acc
            self.user = username
            self.password = passw          
            
            self.save_in_file()
                
        except Exception as e:
            print(f"Error: {e}")



    def save_in_file(self):





        try:              
            flag = os.path.exists(self.file_name)
            with open(self.file_name , "a" ,newline="") as file:
                writer = csv.writer(file)

                if not flag:
                    writer.writerow(["Account", "Name" , "Password"])



                writer.writerow([self.account,self.user,self.password])

        except FileNotFoundError as e:
            print(f"Error: {e}")          
        except Exception as e:
            print(f"Error: {e}")



    def view_save_password(self):

        try:
            with open(self.file_name , "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    print(f"Account name: {row[0]} \nUser Name: {row[1]} \nPassword: {row[2]}")

        except Exception as e:
            print(f"Error: {e}")

        
        
            

if __name__ == "__main__":
    pm = Password_Manager()
    pm.accept_password()
    # pm.view_save_password()

