# YtDwnld (If you see this - This project is now open source!)
from pytubefix import YouTube
import tkinter as tk
import os

title = "Hi"
author = ""
views = ""

def download():
    url = url_box.get()
    yt = YouTube(url)
    title = yt.title
    print(f"Downloading: {title}")


# -- Setting up tkinter --
root = tk.Tk()
root.title("YtDwnld")
root.geometry("400x300")
# ------------------------

# -- Creating UI --
prog_name = tk.Label(root, text="YtDwnld", font=("Arial", 16))
url_box = tk.Entry(root, width=50)
vid_title = tk.Label(root, text=title, font=("Arial", 16))
download_button = tk.Button(root, text="Download!", font=("Arial", 16), command=download)
prog_name.pack()
vid_title.pack()
url_box.pack(pady=84)
download_button.pack()
# -----------------

root.mainloop()