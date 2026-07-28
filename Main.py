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
                username = input("Enter a Username for this password: ")
                if username == "":
                    print("Username canot be empty!")
                else:
                    break

            while True:
                # FOR HIDDING PASWORD GONNA ACTIVATE THIS LATER
                passw = getpass.getpass("Please enter your password: ")
                
                # passw = input("Please enter your password: ")                               
                if passw == "":
                    print("Password canot be empty!")
                else:
                    break
            print("Password has been added!")

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

        

    def search_password(self):
        try:

            flag = os.path.exists(self.file_name)
            if not flag:
                print("No password saved!")


            while True:
                search__account = input("Enter account name you wanna Search: ")
                if search__account == "":
                    print("account name canot be empty!")
                else:
                    break


            while True:
                search__username = input("Enter username you wanna Search: ")
                if search__username == "":
                    print("username name canot be empty!")
                else:
                    break




            with open(self.file_name , "r") as file:
                flag = False
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if search__account == row[0] and  search__username == row[1]:
                        print(f"Your password is: {row[2]}")
                        flag = True
                        break

                if not flag:
                    print("No account found with that name and username")
                    

        except Exception as e:
            print(f"Error: {e}")



    def main(self):

            while True:
                try:
                    
                    print("1. Add new password")
                    print("2. View saved passwords")
                    print("3. Search password")
                    print("4. Exit")

                    option = int(input("Choose any option(1-4): "))

                    if option == 1:
                        self.accept_password()


                    elif option == 2:
                        self.view_save_password()


                    elif option == 3:
                        self.search_password()


                    elif option == 4:
                        print("Thankyou for using our Password Manager!")
                        break

                    else:
                        print("Enter correct option: ")

                except Exception:
                    print("Enter correct option!")


if __name__ == "__main__":
    pm = Password_Manager()
    # pm.accept_password()
    # pm.view_save_password()
    # pm.search_password()
    pm.main()






