import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
# from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showinfo
import sys
import threading

history = []
is_running = False
is_killed = False
current_process: subprocess.Popen | None = None

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


def check_is_running():
    global is_running
    if is_running:
        showinfo("Error", "A command is already running, please wait or kill the command")
        return True
    return False


def do_command_with_thread(command, args=None):
    global is_running
    if check_is_running():
        return
    is_running = True
    thread = threading.Thread(target=do_command, args=(command, args))
    thread.start()


def do_command(command, args=None):
    global is_running
    url_val = get_url()

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} working for url {url_val}\n\n", "green")
    command_textbox.update()

    args = [command] + (args or []) + [url_val]
    print("Running command: ", args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # v2
    global current_process, is_killed
    current_process = p
    while True:
        out = p.stdout.readline()
        if out == b"" and p.poll() is not None:
            break
        if out != b"":
            command_textbox.insert(tk.END, out.decode("utf-8"))
            command_textbox.see(tk.END)
            command_textbox.update()
    return_code = p.poll()
    if is_killed:
        is_killed = False
        print("Error: ", f"{command} was killed")
        command_textbox.insert(tk.END, f"\nprocess killed", "red")
    elif return_code != 0:
        err = p.stderr.readlines()
        err_str = b"\n".join(err).decode("utf-8")
        print("Error: ", err_str)
        command_textbox.insert(tk.END, f"an error occurred during {command}:\n{err_str} with return code {return_code}",
                               "red")
    else:
        command_textbox.insert(tk.END, f"{command} finished", "green")
        command_textbox.see(tk.END)
        command_textbox.update()
        prev = command_textbox.get("1.0", tk.END)
        history.append(prev)
        print("Done")

    is_running = False
    current_process = None


def kill():
    global is_running, is_killed
    if not is_running:
        return
    current_process.kill()
    is_killed = True


# Save function.
def save(content=None):
    if check_is_running():
        return
    filename = asksaveasfilename(
        defaultextension=".txt",
        filetypes=(
            ("Text files", "*.txt"),
            ("Log files", "*.log"),
            ("All files", "*.*"),
        ),
    )
    if filename is None or filename == "":
        return
    file = open(filename, mode="w")
    if not content:
        content = command_textbox.get("1.0", tk.END)

    file.write(content)
    file.close()


fg_color = "sienna"
bg_color = "cornsilk"
font = ("Consolas", 12)

root = tk.Tk()
root.title("IP Tools")
frame = tk.Frame(root, bg=bg_color, bd=10, relief=tk.RIDGE)
frame.grid(row=0, column=0)
controls_frame = tk.Frame(frame, bg=bg_color, pady=5, padx=5)
controls_frame.grid(row=0, column=0)


def create_function_button(text, command, args=None):
    return tk.Button(
        controls_frame,
        fg=fg_color,
        bg="antique white",
        width=33,
        text=text,
        command=lambda: do_command_with_thread(command, args),
        borderwidth=1,
    )


def create_url_entry():
    # decorative label
    url_label = tk.Label(
        controls_frame,
        text="Enter a URL of interest: ",
        compound="center",
        font=font,
        bd=0,
        cursor="heart",
        fg=fg_color,
        bg=bg_color
    )
    url_label.grid(row=1, column=0)
    u_entry = tk.Entry(controls_frame, width=21, font=("", 14), cursor="tcross")  # change font
    u_entry.grid(row=2, column=0)
    return u_entry


def create_command_textbox():
    # Adds an output box to GUI.
    c_textbox = tksc.ScrolledText(frame, font=font)
    c_textbox.tag_config("red", foreground="red")
    c_textbox.tag_config("green", foreground="green")
    c_textbox.grid(row=0, column=1)
    return c_textbox


def create_history_frame():
    h_frame = tk.Frame(root, bg=bg_color, bd=10, relief=tk.RIDGE)
    h_text = tksc.ScrolledText(h_frame, font=font)
    h_text.grid(row=0, column=0)
    history_save_btn = tk.Button(
        h_frame,
        bg="antique white",
        fg=fg_color,
        text="Save",
        command=lambda: save("====================\n".join(history)),
    )
    history_save_btn.grid(row=1, column=0)
    return h_frame, h_text


text_frame = tk.Frame(controls_frame, bg=bg_color)
text_frame.grid(row=0, column=0)
title = tk.Label(text_frame, text="IP Tools", font=(font[0], 20), fg="sienna", height=5, bg=bg_color)
title.grid(row=0, column=0)
url_entry = create_url_entry()
ping_btn = create_function_button("Check to see if a URL is up and active", "ping", ping_args)
ping_btn.grid(row=3, column=0)
nslookup_btn = create_function_button("Get the IP address of a URL", "nslookup")
nslookup_btn.grid(row=4, column=0)
tracert_btn = create_function_button("Get the path of a URL", tracert_cmd, tracert_args)
tracert_btn.grid(row=5, column=0)
save_and_history_frame = tk.Frame(controls_frame)
save_and_history_frame.grid(row=6, column=0)
save_btn = tk.Button(save_and_history_frame, bg="antique white", fg=fg_color, width=10, text="Save", command=save)
save_btn.grid(row=0, column=0)
kill_btn = tk.Button(save_and_history_frame, bg="antique white", fg=fg_color, width=10, text="Kill", command=kill)
kill_btn.grid(row=0, column=2)

command_textbox = create_command_textbox()
history_frame, history_text = create_history_frame()


def show_main():
    history_frame.grid_forget()
    frame.grid(row=0, column=0)


def show_history():
    if check_is_running():
        return
    frame.grid_forget()
    history_frame.grid(row=0, column=0)
    history_text.delete(1.0, tk.END)
    for item in history:
        history_text.insert(tk.END, item)
        history_text.insert(tk.END, "\n====================\n")


back_btn = tk.Button(history_frame, text="Back", bg="antique white", fg=fg_color, command=show_main)
back_btn.grid(row=2, column=0)

history_btn = tk.Button(save_and_history_frame, bg="antique white", fg=fg_color, width=10, text="History",
                        command=show_history)
history_btn.grid(row=0, column=1)

root.mainloop()
