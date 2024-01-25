# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

username = ""
while username.__len__() < 8 or username.__len__() > 24:
    username = input("Enter a username (8-24 characters): ")

password = ""
while (
    password.__len__() < 8
    or password.__len__() > 24
    or password.isalpha()
    or password.isnumeric()
):
    password = input("Enter a password (8-24 characters): ")


# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()
my_auth.set_authorization(username, password)
# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
