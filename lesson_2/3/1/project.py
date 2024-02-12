from PIL import Image, ImageDraw, ImageTk
import math
import tkinter as tk
from tkinter import filedialog, scrolledtext


def offset_array(arr, offset):
    arr = [format(each, "08b") for each in arr]
    arr_join = "".join(arr)
    first = arr_join[:offset]
    last = arr_join[offset:]
    arr_join = last + first

    arr = [arr_join[i:i + 8] for i in range(0, len(arr_join), 8)]
    arr = [int(each, 2) for each in arr]
    return tuple(arr)


def encode(msg, img_path="encoded.png", block_size=20, encode_offset=4, is_ascii_only=True):
    """
    Encode a message into an image
    :param msg: The message to encode
    :param img_path: The path to the image to encode the message into
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

    if encode_offset % 8 == 0 or encode_offset < 0 or encode_offset > 24:
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
    im.save(img_path)
    return im


def decode(img_path="encoded.png"):
    img = Image.open(img_path)
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
                return msg, img

            decoded_array = offset_array(pixel, -encode_offset)
            if is_ascii_only:
                for i in range(3):
                    if decoded_array[i] != 0:
                        msg += chr(decoded_array[i])
            else:
                binary_array = [format(each, "08b") for each in decoded_array]
                binary_string = "".join(binary_array)
                msg += chr(int(binary_string, 2))


root = tk.Tk()
root.title("Image Encoder")

encode_frame = tk.Frame(root)
encode_frame.grid(row=0, column=0)

label = tk.Label(encode_frame, text="Enter the message to encode")
label.pack()

entry = tk.Entry(encode_frame)
entry.pack()

encode_image_label = tk.Label(encode_frame)

encode_image = None


def encode_message():
    msg = entry.get()
    im = encode(msg, encode_offset=10, is_ascii_only=False)
    im = im.resize((200, 200))
    global encode_image
    encode_image = ImageTk.PhotoImage(im)
    encode_image_label.configure(image=encode_image)


button = tk.Button(encode_frame, text="Encode", command=encode_message)
button.pack()
encode_image_label.pack()

decode_frame = tk.Frame(root)
decode_frame.grid(row=0, column=1)

decoded_textbox = scrolledtext.ScrolledText(decode_frame, wrap=tk.WORD)
decode_image_label = tk.Label(decode_frame)

decode_image = None


def decode_message():
    filename = filedialog.askopenfilename(
        initialdir="./",
        title="Select an image to decode", filetypes=[
            ("Image files", "*.png"),
            ("Image files", "*.jpg"),
            ("All files", "*.*")
        ]
    )
    if not filename:
        return
    result, img = decode(filename)
    img = img.resize((200, 200))
    global decode_image
    decode_image = ImageTk.PhotoImage(img)
    decode_image_label.configure(image=decode_image)
    decoded_textbox.delete("1.0", tk.END)
    decoded_textbox.insert(tk.INSERT, result)
    decoded_textbox.see(tk.END)
    decoded_textbox.update()


decode_label = tk.Label(decode_frame, text="Select an image to decode")
decode_label.pack()
decode_button = tk.Button(decode_frame, text="Decode", command=decode_message)
decode_button.pack()
decode_image_label.pack()
decoded_textbox.pack()

root.mainloop()
