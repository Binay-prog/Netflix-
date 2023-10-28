from pathlib import Path
import getpass
import webbrowser
import subprocess

def converter():
    window.destroy()
    subprocess.run(["python", "assets/converter.py"])

def settings():
    window.destroy()
    subprocess.run(["python", "assets/settings.py"])

username = getpass.getuser()

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/home")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Netflix Cookie Checker - Home")

img = PhotoImage(file='assets/home/netflix.png')
window.iconbitmap(default='assets/home/netflix.png')

window.geometry("1090x645+250+250")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=645,
    width=1090,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    545.0,
    322.0,
    image=image_image_1
)

canvas.create_rectangle(
    160.0,
    0.0,
    1098.0,
    645.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    160.0,
    645.0,
    fill="#000000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://netflix.com"),
    relief="flat"
)
button_1.place(
    x=37.0,
    y=29.0,
    width=87.0,
    height=87.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    370.0,
    383.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('import cookies'),
    relief="flat"
)
button_2.place(
    x=184.0,
    y=132.0,
    width=230.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('start'),
    relief="flat"
)
button_3.place(
    x=184.0,
    y=232.0,
    width=230.0,
    height=60.0
)

canvas.create_text(
    204.0,
    342.0,
    anchor="nw",
    text="Output Path",
    fill="#000000",
    font=("SegoeFluentIcons", 20 * -1)
)

canvas.create_text(
    204.0,
    385.0,
    anchor="nw",
    text="Select a folder",
    fill="#000000",
    font=("SegoeFluentIcons", 20 * -1)
)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("same"),
    relief="flat"
)
button_4.place(
    x=42.0,
    y=140.0,
    width=77.0,
    height=77.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: settings(),
    relief="flat"
)
button_5.place(
    x=42.0,
    y=357.0,
    width=77.0,
    height=77.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://discord.com/invite/RSCdKeKB5X"),
    relief="flat"
)
button_6.place(
    x=42.0,
    y=466.0,
    width=77.0,
    height=77.0
)

canvas.create_text(
    195.0,
    29.0,
    anchor="nw",
    text=f"Welcome {username}",
    fill="#FFFFFF",
    font=("Segoe UI Variable", 40 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: converter(),
    relief="flat"
)
button_7.place(
    x=42.0,
    y=249.0,
    width=77.0,
    height=77.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    833.0,
    381.0,
    image=image_image_3
)

canvas.create_text(
    609.0,
    161.0,
    anchor="nw",
    text="---------------",
    fill="#000000",
    font=("Segoe UI Variable", 12 * -1)
)

canvas.create_text(
    595.0,
    100.0,
    anchor="nw",
    text="Log",
    fill="#FFFFFF",
    font=("Segoe UI Variable", 24 * -1)
)

canvas.create_rectangle(
    152.0,
    -1.0,
    153.00003051757812,
    645.0,
    fill="#252525",
    outline="")

canvas.create_text(
    195.0,
    503.0,
    anchor="nw",
    text="Working Cookies :",
    fill="#FFFFFF",
    font=("Segoe UI Variable", 24 * -1)
)

canvas.create_text(
    412.0,
    504.0,
    anchor="nw",
    text="--",
    fill="#FFFFFF",
    font=("Segoe UI Variable", 24 * -1)
)

canvas.create_text(
    400.0,
    556.0,
    anchor="nw",
    text="--",
    fill="#FFFFFF",
    font=("Segoe UI Variable", 24 * -1)
)

canvas.create_text(
    195.0,
    555.0,
    anchor="nw",
    text="Expired Cookies :",
    fill="#FFFFFF",
    font=("Segoe UI Variable", 24 * -1)
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('output folder'),
    relief="flat"
)
button_8.place(
    x=502.0,
    y=377.0,
    width=43.0,
    height=43.0
)
window.resizable(False, False)
window.mainloop()
