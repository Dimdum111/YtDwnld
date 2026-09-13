# YtDwnld (If you see this - This project is now open source!)
import yt_dlp
import tkinter as tk
import os
import static_ffmpeg

static_ffmpeg.add_paths()
output_folder = "YtDwnld Downloads"
os.makedirs("YtDwnld Downloads", exist_ok=True)

ydl_opts = {
    'format': 'bestvideo[vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    'noplaylist': True,
    'merge_output_format': 'mp4',
}

mp3format = "bestaudio/best"
mp4format = "bestvideo[vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

def download():
    url = url_box.get()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        
        title = info.get("title")
        author = info.get("uploader")
        
        vid_title.config(text=title)
        vid_author.config(text=f"By: {author}")
        ydl.download([url])


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
is_mp3 = tk.Checkbutton(root, text="Download as audio? (mp3)")

prog_name.pack()
vid_title.pack()
vid_author.pack()

url_box.pack(pady=16)
download_button.pack(pady=50)
is_mp3.pack()
# -----------------

root.mainloop()