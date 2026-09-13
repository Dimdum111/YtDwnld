# YtDwnld (If you see this - This project is now open source!)
import yt_dlp
import tkinter as tk
import os
import static_ffmpeg
import threading

static_ffmpeg.add_paths()
output_folder = "YtDwnld Downloads"
os.makedirs("YtDwnld Downloads", exist_ok=True)

ydl_opts = {
    'format': 'bestvideo[vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    'noplaylist': True,
    'quiet': True,
    'merge_output_format': 'mp4',
}

mp3format = "bestaudio/best"
mp4format = "bestvideo[vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

def download():
    url = url_box.get()
    format = format_choice.get()
    playlists = playlist_choice.get()
    ydl_opts['noplaylist'] = False if playlists == "1" else True
    
    if format == "1":
        ydl_opts['format'] = mp3format
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    
    else:
        ydl_opts['format'] = mp4format
        ydl_opts['postprocessors'] = []
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            title = info.get("title")
            author = info.get("uploader")
            
            vid_title.config(text=title)
            vid_author.config(text=f"By: {author}")
            ydl.download([url])
        downloading_status.config(text="Downloaded!", fg="Green")

    except yt_dlp.utils.DownloadError as e:
        downloading_status.config(text="Error! Not a valid URL.", fg="Red")
    except Exception as e:
        downloading_status.config(text=f"Unexpected error... {e}", fg="Red")
    finally:
        download_button.config(state="normal")

def start_download():
    downloading_status.config(text="Downloading..", fg="Green")
    download_button.config(state="disabled")
    threading.Thread(target=download, daemon=True).start()


# -- Setting up tkinter --
root = tk.Tk()
root.title("YtDwnld")
root.geometry("400x320")
# ------------------------

# -- Creating UI --
prog_name = tk.Label(root, text="YtDwnld", font=("Arial", 20))
url_box = tk.Entry(root, width=50)
downloading_status = tk.Label(root, text="", font=("Arial", 11))

vid_title = tk.Label(root, text="", font=("Arial", 12))
vid_author = tk.Label(root, text="", font=("Arial", 12))

format_choice = tk.StringVar(value="0")
playlist_choice = tk.StringVar(value="0")

download_button = tk.Button(root, text="Download!", font=("Arial", 16), command=start_download, fg="green")
is_mp3 = tk.Checkbutton(root, text="Download as audio? (mp3)", variable=format_choice)
download_playlists = tk.Checkbutton(root, text="Download entire playlist?", variable=playlist_choice)

prog_name.pack()
vid_title.pack()    
vid_author.pack()

url_box.pack(pady=16)
downloading_status.pack()
download_button.pack(pady=38)
is_mp3.pack()
download_playlists.pack()
# -----------------

root.mainloop()

# This is just a fun project, I just made it for fun and also for myself because i needed a yt downloader