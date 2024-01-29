# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import sys

history = []


def get_url():
    url_val = url_entry.get()
    if len(url_val) == 0:
        url_val = "127.0.0.1"
    return url_val


# Modify the do_command function:
#   to use the new button as needed
def do_command(command, args=None):
    global command_textbox, url_entry
    url_val = get_url()

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} working for url {url_val}\n\n")
    command_textbox.update()

    args = [command, url_val] + (args or [])
    print("Running command: ", args)

    p = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )  # v2
    while True:
        out = p.stdout.readline()
        if out == b"" and p.poll() is not None:
            break
        if out != b"":
            command_textbox.insert(tk.END, out.decode("utf-8"))
            command_textbox.see(tk.END)
            command_textbox.update()

    prev = command_textbox.get("1.0", tk.END)
    history.append(prev)
    print("Done")
    # cmd_results, cmd_errors = p.communicate()
    # command_textbox.insert(tk.END, cmd_results)
    # command_textbox.insert(tk.END, cmd_errors)


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
frame = tk.Frame(root)
frame.pack()

# if it is windows
ping_args = []
ping_times = 5
if sys.platform.startswith("win"):
    root.title("Windows")
    ping_args.append("-n")
elif sys.platform.startswith("darwin"):
    root.title("Mac")
    ping_args.append("-c")
else:
    root.title("Linux")
    ping_args.append("-c")
ping_args.append(str(ping_times))
# set up button to run the do_command function
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active",
                     command=lambda: do_command("ping", ping_args))
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
command_textbox = tksc.ScrolledText(frame)
command_textbox.pack()

save_btn = tk.Button(frame, text="Save", command=save)
save_btn.pack()

history_frame = tk.Frame(root)

history_text = tksc.ScrolledText(history_frame)
history_text.pack()

history_save_btn = tk.Button(history_frame, text="Save", command=lambda: save("====================\n".join(history)))
history_save_btn.pack()

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


back_btn = tk.Button(history_frame, text="Back", command=lambda: show_main())
back_btn.pack()

history_btn = tk.Button(frame, text="History", command=show_history)
history_btn.pack()

root.mainloop()
