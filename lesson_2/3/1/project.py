import pip
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk
import math
import random


def offset_array(arr, offset):
    arr = [format(each, "08b") for each in arr]
    arr_join = "".join(arr)
    first = arr_join[:offset]
    last = arr_join[offset:]
    arr_join = last + first

    arr = [arr_join[i:i + 8] for i in range(0, len(arr_join), 8)]
    arr = [int(each, 2) for each in arr]
    return tuple(arr)


def encode(msg, block_size=20, encode_offset=0, is_ascii_only=False):
    """
    Encode a message into an image
    :param msg: The message to encode
    :param block_size: The size of the color blocks to use
    :param encode_offset: The offset to use when encoding the message
    :param is_ascii_only: Whether to only allow ASCII characters
    """
    characters_as_ints = []
    for cha in msg:
        characters_as_ints.append(ord(cha))
    length = len(characters_as_ints)
    if block_size > 255 or block_size < 0:
        raise ValueError("block_size should be between 0 and 255")

    if encode_offset < 0 or encode_offset > 24:
        raise ValueError("encode_offset should be between 0 and 24 and not a multiple of 8")

    if is_ascii_only:
        if max(characters_as_ints) > 255:
            raise ValueError("The message contains non-ASCII characters, set is_ascii_only to False")
    # calculate the size of the image, +2 to account for the two blocks, one from the beginning and one from the end
    if is_ascii_only:
        s = math.ceil(math.sqrt((length / 3) + 2))
    else:
        s = math.ceil(math.sqrt(length + 2))
    size = (s, s)

    im = Image.new("RGB", (s * block_size, s * block_size), "white")
    draw = ImageDraw.Draw(im)
    index = 0
    pos = 0

    # Draw a block at the given position with the given color
    def draw_block(x, y, color):
        draw.rectangle((
            x * block_size,
            y * block_size,
            x * block_size + block_size - 1,
            y * block_size + block_size - 1
        ), fill=color)

    draw_block(pos % size[0], pos // size[0], (block_size, encode_offset, 255 if is_ascii_only else 0))
    pos += 1
    while True:
        temp = [0, 0, 0]
        # If the message is ASCII only, we can encode 3 characters per block
        if is_ascii_only:
            for i in range(3):
                if index < len(characters_as_ints):
                    temp[i] = characters_as_ints[index]
                    index += 1
                else:
                    break
            else:
                draw_block(pos % size[0], pos // size[0], offset_array(temp, encode_offset))
                pos += 1
                continue
            draw_block(pos % size[0], pos // size[0], offset_array(temp, encode_offset))
            pos += 1
            draw_block(pos % size[0], pos // size[0], (0, 0, 0))
            break
        else:
            # If the message is not ASCII only, we can only encode 1 character per block
            if index >= length:
                draw_block(pos % size[0], pos // size[0], (0, 0, 0))
                break

            binary_string = format(characters_as_ints[index], "08b").zfill(24)
            binary_string = binary_string[encode_offset:] + binary_string[:encode_offset]
            temp = [int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8)]
            if len(temp) < 3:
                temp += [0] * (3 - len(temp))
            draw_block(pos % size[0], pos // size[0], tuple(temp))
            pos += 1
            index += 1
    return im


def decode(img):
    width, height = img.size
    msg = ""
    first_pixel = img.getpixel((0, 0))
    block_size = first_pixel[0]
    encode_offset = first_pixel[1]
    is_ascii_only = first_pixel[2] == 255

    for y in range(height // block_size):
        for x in range(width // block_size):
            if x == 0 and y == 0:
                continue
            pixel = img.getpixel((x * block_size, y * block_size))
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                return msg

            decoded_array = offset_array(pixel, -encode_offset)
            if is_ascii_only:
                for i in range(3):
                    if decoded_array[i] != 0:
                        msg += chr(decoded_array[i])
            else:
                binary_array = [format(each, "08b") for each in decoded_array]
                binary_string = "".join(binary_array)
                msg += chr(int(binary_string, 2))


try:
    import customtkinter as ctk

    print("Found installed package.")
except ModuleNotFoundError:
    print("Module not found, installing...")
    pip.main(["install", "customtkinter"])
    import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("560x530")

raw_image = Image.new("RGB", (200, 200), "white")
image = ctk.CTkImage(raw_image, size=(200, 200))
app.after(300, lambda: app.iconphoto(False, ImageTk.PhotoImage(raw_image)))


def action(name):
    global image, raw_image
    if name == "encode":
        text = textbox.get("1.0", "end-1c")
        if not text:
            return
        try:
            block_size = int(image_size_entry.get())
            if block_size < 0 or block_size > 255:
                messagebox.showerror("Error", "Invalid block size")
                return
            ascii_only = True if ascii_only_checkbox.get() == 1 else False
            print(ascii_only)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")
            return
        offset = random.randint(0, 24)
        raw_image = encode(text, block_size, offset, ascii_only)
        image = ctk.CTkImage(raw_image, size=(200, 200))
        image_label.configure(image=image)
        app.iconphoto(False, ImageTk.PhotoImage(raw_image))
    else:
        if not raw_image:
            return
        msg = decode(raw_image)
        if not msg:
            messagebox.showerror("Error", "No message found in the image")
            return
        textbox.delete("1.0", "end")
        textbox.insert("1.0", msg)
        textbox.update()


def change_mode(name):
    action_button.configure(text=name)
    textbox.delete("1.0", "end")
    global image, raw_image
    raw_image = Image.new("RGB", (200, 200), "white")
    image = ctk.CTkImage(raw_image, size=(200, 200))
    image_label.configure(image=image)
    textbox.grid_forget()
    action_label.grid_forget()
    action_button.grid_forget()
    save_image_button.grid_forget()
    select_image_button.grid_forget()
    image_label.grid_forget()
    if name == "Encode":
        app.title("Image Encoder")
        content_frame.pack_forget()
        encode_option_frame.pack(pady=10, padx=60, fill="both", expand=True)
        content_frame.pack(pady=10, padx=60, fill="both", expand=True)
        action_label.configure(text="Enter the message to encode:")
        action_label.grid(row=0, column=0)
        textbox.grid(row=1, column=0, padx=10, pady=10)
        image_label.grid(row=1, column=1, padx=10, pady=10)
        action_button.grid(row=2, column=0, padx=10, pady=10)
        save_image_button.grid(row=2, column=1, padx=10, pady=10)
    else:
        app.title("Image Decoder")
        encode_option_frame.pack_forget()
        action_label.configure(text="Select an image to decode:")
        action_label.grid(row=0, column=0)
        image_label.grid(row=1, column=0, padx=10, pady=10)
        textbox.grid(row=1, column=1, padx=10, pady=10)
        select_image_button.grid(row=2, column=0, padx=10, pady=10)
        action_button.grid(row=2, column=1, padx=10, pady=10)


def select_image():
    filename = ctk.filedialog.askopenfilename(
        initialdir="./",
        title="Select an image to decode", filetypes=[
            ("Image files", "*.png"),
            ("Image files", "*.jpg"),
            ("All files", "*.*")
        ]
    )
    if not filename:
        return
    global image, raw_image
    raw_image = Image.open(filename)
    image = ctk.CTkImage(raw_image, size=(200, 200))
    image_label.configure(image=image)


def save_image():
    filename = ctk.filedialog.asksaveasfilename(
        initialdir="./",
        initialfile="output.png",
        title="Save the image",
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPG files", "*.jpg")
        ]
    )
    print(filename)
    if not filename:
        return
    raw_image.save(filename)


selection_frame = ctk.CTkFrame(master=app)
selection_frame.pack(pady=10, padx=60, fill="both", expand=True)

selection_title_label = ctk.CTkLabel(master=selection_frame, text="Select a mode:")
selection_title_label.pack(side="top")

encode_option_frame = ctk.CTkFrame(master=app, height=100)

image_size_label = ctk.CTkLabel(master=encode_option_frame, text="Image size per small block: (0-255)")
image_size_label.grid(row=0, column=0, padx=10, pady=10)
image_size_entry = ctk.CTkEntry(master=encode_option_frame, placeholder_text="Image size")
image_size_entry.insert(0, "20")
image_size_entry.grid(row=0, column=1, padx=10, pady=10)
ascii_label = ctk.CTkLabel(master=encode_option_frame, text="Is English only? (True/False)")
ascii_label.grid(row=1, column=0, padx=10, pady=10)
ascii_only_checkbox = ctk.CTkCheckBox(
    master=encode_option_frame,
    text=""
)
ascii_only_checkbox.grid(row=1, column=1, padx=10, pady=10)

content_frame = ctk.CTkFrame(master=app)


radiobutton_var = ctk.StringVar(value="encode")
textbox = ctk.CTkTextbox(master=content_frame)

action_button = ctk.CTkButton(
    master=content_frame,
    text="Encode",
    command=lambda: action(radiobutton_var.get()),
)

radiobutton_1 = ctk.CTkRadioButton(
    master=selection_frame,
    text="Encode",
    variable=radiobutton_var,
    value="encode",
    command=lambda: change_mode("Encode")
)

radiobutton_2 = ctk.CTkRadioButton(
    master=selection_frame,
    text="Decode",
    variable=radiobutton_var,
    value="decode",
    command=lambda: change_mode("Decode")
)

action_label = ctk.CTkLabel(master=content_frame)
select_image_button = ctk.CTkButton(master=content_frame, text="Select an image", command=select_image)
image_label = ctk.CTkLabel(master=content_frame, image=image, text="", width=200, height=200)
save_image_button = ctk.CTkButton(master=content_frame, text="Save image", command=save_image)

radiobutton_1.pack(side="left", padx=10, pady=10)
radiobutton_2.pack(side="right", padx=10, pady=10)
change_mode("Encode")

app.mainloop()
