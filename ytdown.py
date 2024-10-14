import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import os

def download_video():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    if url and save_path:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(save_path)
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a URL and select a save location.")

def download_audio():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    if url and save_path:
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download(save_path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            messagebox.showinfo("Success", "Audio downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a URL and select a save location.")


root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x150")


url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

video_button = tk.Button(root, text="Download Video", command=download_video)
video_button.pack(pady=5)

audio_button = tk.Button(root, text="Download Audio", command=download_audio)
audio_button.pack(pady=5)


root.mainloop()