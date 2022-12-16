
import pandas as pd


def main():
    totalamount = 0
    while True:
        print("Please choose what you want to have : - \n")
        print("1. Starters \n")
        print("2. Main Course \n")
        print("3. Desserts \n")
        print("4. Exit")

        b = input()

        if b == '1':
            print("Starters \n")

            starters = {'Item': ['Panner Tikka', 'Mushroom Tikka', 'Chicken Chilly', 'Chicken 65', 'Hara Bara Kebab'],
                        'Amount': [200, 180, 230, 250, 190]}

            starter_df = pd.DataFrame(starters)

            print(starter_df,"\n")

            print("Do you wish to select any of the times ? Please enter the name of the dish \n")
            item1 = input("")
            print("No. of dishes \n")
            noofitems = int(input(""))

            for i , j in zip(starters['Item'],starters['Amount']):
                if item1 == i:
                    totalamount += j * noofitems

        elif b == '2':
            print("Main Course \n")

            main_course = {'Item': ['Panner Tikka Masala', 'Mushroom Kadhai', 'Chicken Chilly Manchurian',
                                    'Chicken Masala', 'Mix Veg Masala'],
                        'Amount':  [250, 230, 280, 250, 150]}

            main_course_df = pd.DataFrame(main_course)

            print(main_course_df)

            print("Do you wish to select any of the times ? Please enter the name of the dish \n")
            item1 = input("")
            print("No. of dishes \n")
            noofitems = int(input(""))

            for i, j in zip(main_course['Item'], main_course['Amount']):
                print(i,j)
                if item1 == i:
                    totalamount += j * noofitems



        elif b == '3':
            print("Desserts \n")

            desserts = {'Item': ['Kulfi', 'Ice Cream', 'Ice Cream Cone',
                                    'Faluda', 'Gulab Jamun'],
                           'Amount': [195, 185, 235, 150, 100]}

            desserts_df = pd.DataFrame(desserts)

            print(desserts_df)

            print("Do you wish to select any of the times ? Please enter the name of the dish \n")
            item1 = input("")
            print("No. of dishes \n")
            noofitems = int(input(""))

            for i, j in zip(desserts['Item'], desserts['Amount']):
                if item1 == i:
                    totalamount += j * noofitems
        else:
            break

    print("Total Bill : ",totalamount)

# ------------------ Food Menu System --------------------

print("\n Hi , Welcome to Pinak and Romanch Food Menu System. \n")


df = pd.read_csv(r"C:\Users\hada_a\Desktop\FOS.csv")


dict1 = df.to_dict()

print(" Do you want to :- \n")
print(" 1. Register ")
print(" 2. Login  \n")

a = input()

# ------------------ Register -----------------------

if a == '1':
    new_username = input("Please enter your name : \n")
    new_password = input("Please enter a new password : \n")
    confirmpassword = input("Please re-enter your password : \n")
    if new_password == confirmpassword:
        row = pd.Series([new_username,new_password],index=df.columns)
        df = df.append(row,ignore_index=True)
        print(df,"\n")
        df.to_csv(r"C:\Users\hada_a\Desktop\FOS.csv", mode='w', index=False, header=True)
        print("Row Added Successfully")
    else:
        print("Passwords doesn't Match \n")

# ------------------ Login -----------------------

elif a == '2':
    print("Please Enter username : \n")
    login_username = input("")
    print("Please Enter password : \n")
    login_password = input("")
    userNameFound = False
    for i in dict1['username'].keys():
        if dict1['username'][i] == login_username:
            userNameFound = True
            if dict1['password'][i] == login_password:
                print("Success")
                main()
            else:
                print("Invalid Password")
    if not userNameFound:
        print("Invalid Username")




