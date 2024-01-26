# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import os


history = []
# Modify the do_command function:
#   to use the new button as needed
def do_command(command, args=None):
    global command_textbox, url_entry
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()
    url_val = url_entry.get()
    if len(url_val) == 0:
        url_val = "127.0.0.1"
    args = [command, url_val] + (args or [])
    
    p = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )  # v2
    while True:
        out = p.stdout.readline()
        print(out)
        if out == b"" and p.poll() is not None:
            break
        if out != b"":
            command_textbox.insert(tk.END, out)
            command_textbox.see(tk.END)
            command_textbox.update()

    prev = command_textbox.get("1.0", tk.END)
    history.append(prev)
    print("Done")
    # cmd_results, cmd_errors = p.communicate()
    # command_textbox.insert(tk.END, cmd_results)
    # command_textbox.insert(tk.END, cmd_errors)


# Save function.
def mSave():
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
    text_to_save = command_textbox.get("1.0", tk.END)

    file.write(text_to_save)
    file.close()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda: do_command("ping", ["-t", "10"]))
ping_btn.pack()

nslookup_btn = tk.Button(frame, text="nslookup", command=lambda: do_command("nslookup"))
nslookup_btn.pack()

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
    fg="mediumpurple3"
)
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(frame_URL, font=("comic sans", 14))  # change font
url_entry.pack(side=tk.LEFT)

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

save_btn = tk.Button(frame, text="Save", command=mSave)
save_btn.pack()

history_frame = tk.Frame(root)

history_text = tksc.ScrolledText(history_frame, height=10, width=100)
history_text.pack()

def show_history():
    frame.pack_forget()
    history_frame.pack()
    history_text.delete(1.0, tk.END)
    for item in history:
        history_text.insert(tk.END, item)
        history_text.insert(tk.END, "\n\n")
    

history_btn = tk.Button(frame, text="History", command=show_history)
history_btn.pack()

root.mainloop()
