
import numpy as np
import pandas as pd

# ------------------ Food Menu System --------------------

print("\nHi , Welcome to Pinak and Romanch Food Menu System. \n")

# ------------------ Register -----------------------

df = pd.read_csv(r"C:\Users\Aditya\Desktop\FOS.csv")
print(df)

print(" Do you want to :- \n")
print(" 1. Register ")
print(" 2. Login  \n")

a = input()
print(a)

if a == '1':
    new_username = input("Please enter your name : \n")
    new_password = input("Please enter a new password : \n")
    confirmpassword = input("Please re-enter your password : \n")
    if new_password == confirmpassword:
        row = pd.Series([new_username,new_password],index=df.columns)
        df = df.append(row,ignore_index=True)
        print(df)
        df.to_csv(r"C:\Users\Aditya\Desktop\FOS.csv", mode='a', index=False, header=False)
        print("Row Added Successfully")