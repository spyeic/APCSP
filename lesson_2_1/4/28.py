import tkinter as tk

size = 400
root = tk.Tk()
root.geometry(f"{size}x{size}")


blue_frame = tk.Frame(root, bg="blue", width=size / 4 * 2.5, height=size / 2)
blue_frame.grid(row=0, column=0)

red_frame = tk.Frame(root, bg="red", width=size / 4 * 2.5, height=size / 2)
red_frame.grid(row=1, column=0)

green_frame = tk.Frame(root, bg="green", width=size / 2, height=size / 2)
green_frame.grid(row=0, column=1)

yellow_frame = tk.Frame(root, bg="yellow", width=size / 2, height=size / 2)
yellow_frame.grid(row=1, column=1)

root.mainloop()
