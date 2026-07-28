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




    def update_password(self):
        try:
        
            flag1 = os.path.exists(self.file_name)
            if not flag1:
                print("No password saved!")
                return

            while True:
                updt__account = input("Enter the account name you want to update: ")
                if updt__account == "":
                    print("Account name canot be empty!")
                else:
                    break

            while True:
                updt__username = input("Enter the username of the account you want to update: ")
                if updt__username == "":
                    print("Username name canot be empty!")
                else:
                    break

            exsist = False
            with open(self.file_name , "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0].lower() == updt__account.lower() and  row[1].lower() == updt__username.lower():
                        while True:
                            old__password = input("Enter your old password: ")
                            if old__password == "":
                                print("Password canot be empty!")

                            if row[2] == old__password:
                                exsist = True
                                break
                        
                            # if exsist:
                            #     break        




            if exsist:

                while True:
                    updt__password = input("Enter the updated password: ")
                    if updt__password == "":
                        print("Password canot be empty!")
                    else:
                        break
            
                                            


                with open(self.file_name , "r") as read_file:
                    rows = list(csv.reader(read_file))


                    flag2 = False
                    for row in rows:
                        if row[0].lower() == updt__account.lower() and  row[1].lower() == updt__username.lower():
                            row[2] = updt__password
                            flag2 = True
                            break
                
                with open(self.file_name , "a" , newline="") as write_file:
                    csv_writer = csv.writer(write_file)
                    csv_writer.writerows(rows)    
                
                if flag2:
                    print("Password updated successfully.")


                
            else:
                print("No matching account was found.")



        except Exception as e:
            print(f"Error: {e}")

        except FileNotFoundError as e:
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