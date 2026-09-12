# YtDwnld (If you see this - This project is now open source!)
from pytubefix import YouTube
import tkinter as tk
import os

os.makedirs("YtDwnld Downloads", exist_ok=True)

def download():
    url = url_box.get()
    yt = YouTube(url)
    title, author = yt.title, yt.author
    vid_title.config(text=title)
    vid_author.config(text=f"By: {author}")
    print(f"Downloading: {title}")


# -- Setting up tkinter --
root = tk.Tk()
root.title("YtDwnld")
root.geometry("400x300")
# ------------------------

# -- Creating UI --
prog_name = tk.Label(root, text="YtDwnld", font=("Arial", 20))
url_box = tk.Entry(root, width=50)

vid_title = tk.Label(root, text="", font=("Arial", 12))
vid_author = tk.Label(root, text="", font=("Arial", 12))

download_button = tk.Button(root, text="Download!", font=("Arial", 16), command=download, fg="green")
# is_mp3 = tk.Checkbutton(root, text="Download as audio? (mp3)")

prog_name.pack()
vid_title.pack()
vid_author.pack()

url_box.pack(pady=16)
download_button.pack(pady=50)
# is_mp3.pack()
# -----------------

root.mainloop()