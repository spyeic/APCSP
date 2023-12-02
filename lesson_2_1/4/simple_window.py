#   A program creates a window on your screen using Tkinter.
import tkinter as tk


def test_my_button():
    frame_auth.tkraise()
    # TODO: Use get method of ent_password when the button is pressed, and store result
    user_pwd = ent_pwd.get()
    # TODO: Configure the label in frame_auth to display the password
    lbl_show_password.config(text=user_pwd)


# main window
root = tk.Tk()
root.wm_geometry("400x200")
root.title("Authorization")

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text="Username:")
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=100, pady=5)

lbl_pwd = tk.Label(frame_login, text="Password:")
lbl_pwd.pack()

ent_pwd = tk.Entry(frame_login, bd=3, show="*")
ent_pwd.pack(pady=5)

btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack()

# TODO: Add a label to frame_auth
lbl_show_password = tk.Label(frame_auth, text="nothing")
lbl_show_password.pack()

frame_login.tkraise()
root.mainloop()
