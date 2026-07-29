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
                try:
                        
                    flag = False
                    username = input("Enter a Username for this password: ")
                    if username == "":
                        print("Username canot be empty!")
                        continue
                    if os.path.exists(self.file_name):
                        with open(self.file_name , "r") as file:
                            reader = csv.reader(file)
                            next(reader)
                            for key in reader:
                                if key[0].lower() == acc.lower() and key[1] == username:
                                    print("Account already exists with same username and account!")
                                    flag = True
                                    break

                    
                    if not flag:
                        break
                except Exception as e:
                    print(f"Error: {e}")




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

                if not flag or os.path.getsize(self.file_name) == 0:
                        writer.writerow(["Account", "Name" , "Password"])



                writer.writerow([self.account,self.user,self.password])

        except FileNotFoundError as e:
            print(f"Error: {e}")          
        except Exception as e:
            print(f"Error: {e}")



    def view_save_password(self):

        try:
            if not os.path.exists(self.file_name):
                print("No data saved yet!")
                return
            
            with open(self.file_name , "r") as file:
                reader = file.read().strip()

                if not reader or reader == "Account,Name,Password":
                    print("No data saved yet!")
                    return

            
            for row in self.load_data()[1:]:
                print("--------------------------------")
                print(f"Account name: {row[0]} \nUser Name: {row[1]} \nPassword: {row[2]}")
                print("--------------------------------")
                    

        except Exception as e:
            print(f"Error: {e}")

        

    def search_password(self):
        try:

            flag = os.path.exists(self.file_name)
            if not flag:
                print("No password saved!")
                return


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
                    if search__account.lower() == row[0].lower() and  search__username.lower() == row[1].lower():
                        print(f"Your password is: {row[2]}")
                        flag = True
                        break

                if not flag:
                    print("No account found with that name and username")
                    

        except Exception as e:
            print(f"Error: {e}")



    def delete_user(self):
        try:
        
            flag = os.path.exists(self.file_name)
            if not flag:
                print("No password saved!")
                return

            while True:
                del__account = input("Enter account name you wanna delete: ")
                if del__account == "":
                    print("account name canot be empty!")
                else:
                    break

            while True:
                del__username = input("Enter username you wanna delete: ")
                if del__username == "":
                    print("username name canot be empty!")
                else:
                    break


            flag = False
            with open(self.file_name , "r") as read_file:
                rows = list(csv.reader(read_file))

            with open(self.file_name , "w" , newline="") as write_file:
                csv_writer = csv.writer(write_file)

                for row in rows:
                    if row[0].lower() == del__account.lower() and  row[1].lower() == del__username.lower():
                        flag = True
                        continue
                    csv_writer.writerow(row)

            if flag:
                print("Account deleted successfully.")
            else:
                print("No matching account was found.")
             
        except Exception as e:
            print(f"Error: {e}")

        except FileNotFoundError as e:
            print(f"Error: {e}")


    def load_data(self):

        try:

            if os.path.exists(self.file_name):
                with open(self.file_name , "r") as file:
                    rows = list(csv.reader(file))

                return rows

        except Exception as e:
            print(f"Error: {e}")









    def update_password(self):
        try:
            if not os.path.exists(self.file_name) or os.path.getsize(self.file_name) == 0:
                print("No password saved!")
                return

            while True:
                updt_account = input("Enter the account name you want to update: ")
                if updt_account == "":
                    print("Account name cannot be empty!")
                else:
                    break

            while True:
                updt_username = input("Enter the username of the account you want to update: ")
                if updt_username == "":
                    print("Username cannot be empty!")
                else:
                    break

            with open(self.file_name, "r") as file:
                reader = list(csv.reader(file))

            account_found = False
            password_correct = False
            row_index = None

            for index, row in enumerate(reader[1:], start=1):
                if row[0].lower() == updt_account.lower() and row[1].lower() == updt_username.lower():
                    account_found = True
                    row_index = index
                    correct_row = row

                    while True:
                        old_password = input("Enter your old password: ")

                        if old_password == "":
                            print("Password cannot be empty!")
                            continue

                        break

                    if old_password == correct_row[2]:
                        password_correct = True
                    else:
                        print("Old password is incorrect")

                    break

            if not account_found:
                print("Account name or username is incorrect!")
                return

            if not password_correct:
                return

            while True:
                new_password = input("Enter the updated password: ")

                if new_password == "":
                    print("Password cannot be empty!")
                else:
                    break

            reader[row_index][2] = new_password

            with open(self.file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(reader)

            print("Password updated successfully!")

        except FileNotFoundError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")

    





    def main(self):

            while True:
                try:
                    
                    print("1. Add new password")
                    print("2. View saved passwords")
                    print("3. Search password")
                    print("4. Delete password")
                    print("5. Update password")
                    print("6. Exit")

                    option = int(input("Choose any option(1-6): "))

                    if option == 1:
                        self.accept_password()


                    elif option == 2:
                        self.view_save_password()


                    elif option == 3:
                        self.search_password()


                    elif option == 4:
                        self.delete_user()

                    elif option == 5:
                        self.update_password()                

                    elif option == 6:
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
    # pm.delete_user()
    # pm.update_password()
    pm.main()