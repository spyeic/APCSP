# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import sys

history = []

ping_args = []
ping_times = 5
tracert_cmd = "traceroute"
tracert_args = []
if sys.platform.startswith("win"):
    ping_args.append("-n")
    tracert_cmd = "tracert"
else:
    ping_args.append("-c")
    tracert_args.append("-I")
ping_args.append(str(ping_times))


def get_url():
    url_val = url_entry.get()
    if len(url_val) == 0:
        url_val = "127.0.0.1"
    return url_val


def do_command(command, args=None):
    global command_textbox, url_entry
    url_val = get_url()

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} working for url {url_val}\n\n")
    command_textbox.update()

    args = [command, url_val] + (args or []) 
    print("Running command: ", args)

    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # v2
    while True:
        out = p.stdout.readline()
        if out == b"" and p.poll() is not None:
            break
        if out != b"":
            command_textbox.insert(tk.END, out.decode("utf-8"))
            command_textbox.see(tk.END)
            command_textbox.update()
    err = p.stderr.readlines()
    if err:
        err_str = b"\n".join(err).decode("utf-8")
        print("Error: ", err_str)
        command_textbox.insert(tk.END, f"an error occured during {command}:\n{err_str}", "red")
    else:
        command_textbox.insert(tk.END, f"{command} finished", "green")
        command_textbox.see(tk.END)
        command_textbox.update()
        prev = command_textbox.get("1.0", tk.END)
        history.append(prev)
        print("Done")


# Save function.
def save(content=None):
    filename = asksaveasfilename(
        defaultextension=".txt",
        filetypes=(
            ("Text files", "*.txt"),
            ("Python files", "*.py *.pyw"),
            ("All files", "*.*"),
        ),
    )
    if filename is None:
        return
    file = open(filename, mode="w")
    if not content:
        content = command_textbox.get("1.0", tk.END)

    file.write(content)
    file.close()


root = tk.Tk()
root.title("GUI")
frame = tk.Frame(root)
frame.pack()


def create_function_button(text, command, args=None):
    btn = tk.Button(frame, text=text, command=lambda: do_command(command, args))
    btn.pack()


def create_url_entry():
    # creates the frame with label for the text box
    frame_URL = tk.Frame(frame, pady=10)  # change frame color
    frame_URL.pack()

    # decorative label
    url_label = tk.Label(
        frame_URL,
        text="Enter a URL of interest: ",
        compound="center",
        font=("comic sans", 14),
        bd=0,
        relief=tk.FLAT,
        cursor="heart",
        fg="red"
    )
    url_label.pack(side=tk.LEFT)
    global url_entry
    url_entry = tk.Entry(frame_URL, font=("comic sans", 14))  # change font
    url_entry.pack(side=tk.LEFT)
    return url_entry


def create_command_textbox():
    global command_textbox
    # Adds an output box to GUI.
    command_textbox = tksc.ScrolledText(frame)
    command_textbox.tag_config("red", foreground="red")
    command_textbox.tag_config("green", foreground="green")
    command_textbox.pack()
    save_btn = tk.Button(frame, text="Save", command=save)
    save_btn.pack()


def create_history_frame():
    global history_frame, history_text
    history_frame = tk.Frame(root)
    history_text = tksc.ScrolledText(history_frame)
    history_text.pack()

    history_save_btn = tk.Button(
        history_frame,
        text="Save",
        command=lambda: save("====================\n".join(history)),
    )
    history_save_btn.pack()


create_url_entry()
create_function_button("Check to see if a URL is up and active", "ping", ping_args)
create_function_button("Get the IP address of a URL", "nslookup")
create_function_button("Get the path of a URL", tracert_cmd, tracert_args)
# Adds an output box to GUI.
create_command_textbox()
create_history_frame()


def show_main():
    history_frame.pack_forget()
    frame.pack()


def show_history():
    frame.pack_forget()
    history_frame.pack()
    history_text.delete(1.0, tk.END)
    for item in history:
        history_text.insert(tk.END, item)
        history_text.insert(tk.END, "====================\n\n")


back_btn = tk.Button(history_frame, text="Back", command=show_main)
back_btn.pack()

history_btn = tk.Button(frame, text="History", command=show_history)
history_btn.pack()

root.mainloop()
