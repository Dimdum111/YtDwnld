# YtDwnld (If you see this - This project is now open source!)
from pytubefix import YouTube
import tkinter as tk

# -- Setting up tkinter --
root = tk.Tk()
root.title("YtDwnld")
root.geometry("400x300")
# ------------------------

# -- Creating UI --
prog_name = tk.Label(root, text="YtDwnld", font=("Arial", 16))
url_box = tk.Entry(root, width=50)
prog_name.pack()
url_box.pack(pady=64)
# -----------------

root.mainloop()

# url = input("Enter video URL: ")
# yt = YouTube(url)
# v_title, v_author, v_views = yt.title, yt.author, yt.views

# print("--=[ VIDEO INFO ]=--")
# print(f"{v_title} by {v_author}")
# print(f"Views: {v_views}")