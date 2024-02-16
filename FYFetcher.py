# FYFetcher a simple GUI YouTube Download, which I create in Tkinter Python.

import os
import webbrowser
import wget
import threading
from tkinter.ttk import Button, Label, Checkbutton, Scrollbar
from tkinter import Tk, END, NORMAL, DISABLED, Menu, Toplevel, StringVar, Text, filedialog, messagebox, LabelFrame
from pytube import YouTube

License = """
MIT License

Copyright (c) 2024 Jeremy@JYL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

version = "v0.0.1"

# Create the main window
root = Tk()
# Main window title
root.title("FYFetcher")
# Set the window to unresizeable
root.resizable(width=False, height=False)

# Error handling


def error_handle(error):
    messagebox.showerror("Error", error)

# Download the video


def download_youtube():
    try:
        # Get the link from the link box
        link = input_link.get("1.0", "end-1c")
        # Get the path from the path box
        path_download = path_text.get("1.0", "end-1c")
        # Close the start download window
        New.destroy()
        # Write Started in the log
        output["state"] = NORMAL
        output.insert(END, link + " Started!\n")
        output["state"] = DISABLED
        # Connect to the YouTube
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        # Download the video from YouTube
        video.download(path_download)
        # Write Finish in the log
        output["state"] = NORMAL
        output.insert(END, link + " Finish!\n")
        output["state"] = DISABLED
    except Exception as e:
        error_handle(e)

# Download the audio


def download_audio():
    try:
        # Get the link from the link box
        link = input_link.get("1.0", "end-1c")
        # Get the path from the path box
        path_download = path_text.get("1.0", "end-1c")
        # Close the start download window
        New.destroy()
        # Write Started in the log
        output["state"] = NORMAL
        output.insert(END, link + " Started!\n")
        output["state"] = DISABLED
        # Connect to the YouTube
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first()
        # Download the audio from YouTube
        audio.download(path_download)
        # Write Finish in the log
        output["state"] = NORMAL
        output.insert(END, link + " Finish!\n")
        output["state"] = DISABLED
    except Exception as e:
        error_handle(e)

# Download the file


def download_file():
    try:
        # Get the link from the link box
        link = input_link.get("1.0", "end-1c")
        # Get the path from the path box
        path_download = path_text.get("1.0", "end-1c")
        # Close the start download window
        New_Download.destroy()
        # Write Started in the log
        output["state"] = NORMAL
        output.insert(END, link + " Started!\n")
        output["state"] = DISABLED
        # Download the file via wget
        wget.download(link, path_download, bar=None)
        # Write Finish in the log
        output["state"] = NORMAL
        output.insert(END, link + " Finish!\n")
        output["state"] = DISABLED
    except Exception as e:
        error_handle(e)

# Set the path


def path():
    global download_path
    # Ask the path from the user
    download_path = filedialog.askdirectory()
    # Insert the text to the path box
    path_text.insert(END, download_path)

# Thread to download the video


def start_t():
    # Create the thread
    download_t = threading.Thread(target=download_youtube)
    # Start the thread
    download_t.start()

# Thread to download the audio


def start_t_a():
    # Create the thread
    download_t_a = threading.Thread(target=download_audio)
    # Start the thread
    download_t_a.start()

# Thread to download file


def start_t_download():
    # Create the thread
    download_t_file = threading.Thread(target=download_file)
    download_t_file.start()

# Clear the log box


def clear():
    output["state"] = NORMAL
    output.delete("1.0", END)
    output["state"] = DISABLED


# Check the check box for download video or audio


def a_or_v():
    if audio_video.get() == "1":
        start_t_a()
    elif audio_video.get() == "":
        start_t()

# Create a new window for start new download


def new_video():
    global path_text, input_link, New, audio_video
    audio_video = StringVar()
    # Create the window
    New = Toplevel()
    # New window title
    New.title("New Download")
    # Set the window to unresizeable
    New.resizable(width=False, height=False)
    # New windows subtitle
    Label(New, text="New YouTube Download").grid(column=1, row=0, columnspan=3)
    # Create the link label
    Label(New, text="Link:").grid(column=0, row=1, padx=2.5)
    # Create the link box
    input_link = Text(New, height=1, width=40)
    input_link.grid(column=1, row=1, columnspan=3, padx=2.5, pady=2.5)
    # Create the button to input the path
    Button(New, text="Path", command=path, width=2.5).grid(
        column=0, row=2, padx=2.5)
    # Create the path box
    path_text = Text(New, height=1, width=40)
    path_text.grid(column=1, row=2, columnspan=3)
    # Create the download button
    Button(New, text="Download", command=a_or_v,
           width=2.5).grid(column=2, row=3)
    # Create the download audio check box
    Checkbutton(New, text='Audio Only',
                variable=audio_video).grid(column=1, row=3)
    # Create the cancel button
    Button(New, text="Cancel", command=New.destroy,
           width=2.5).grid(column=3, row=3, padx=5)


def new_download():
    global path_text, input_link, New_Download
    # Create the window
    New_Download = Toplevel()
    # New window title
    New_Download.title("New Download")
    # Set the window to unresizeable
    New_Download.resizable(width=False, height=False)
    # New windows subtitle
    Label(New_Download, text="New Download").grid(
        column=1, row=0, columnspan=3)
    # Create the link label
    Label(New_Download, text="Link:").grid(column=0, row=1, padx=2.5)
    # Create the link box
    input_link = Text(New_Download, height=1, width=40)
    input_link.grid(column=1, row=1, columnspan=3, padx=2.5, pady=2.5)
    # Create the button to input the path
    Button(New_Download, text="Path", command=path, width=2.5).grid(
        column=0, row=2, padx=2.5)
    # Create the path box
    path_text = Text(New_Download, height=1, width=40)
    path_text.grid(column=1, row=2, columnspan=3)
    # Create the download button
    Button(New_Download, text="Download", command=start_t_download,
           width=2.5).grid(column=1, row=3)
    # Create the cancel button
    Button(New_Download, text="Cancel", command=New_Download.destroy,
           width=2.5).grid(column=2, row=3, padx=5)

# Help


def help_link():
    webbrowser.open("https://github.com/Jeremy-JYL/FYFetcher/wiki")

# Update


def update():
    try:
        wget.download(
            "https://raw.githubusercontent.com/Jeremy-JYL/FYFetcher/main/version", bar=None)
        with open("version", "r") as f:
            ver = f.read()
        os.remove("version")

        if ver.find(version) == 0:
            messagebox.showinfo(
                "Update", f"FYFetcher is the newest version!\n({version})")
        else:
            result = messagebox.askyesno(
                "Update", f"FYFetcher have a new update! ({ver.split()[0]})\nUpgrade?")
            if result:
                wget.download(
                    "https://raw.githubusercontent.com/Jeremy-JYL/FYFetcher/main/FYFetcher.py", "tmp.py", bar=None)
                os.remove("FYFetcher.py")
                os.rename("tmp.py", "FYFetcher.py")
                exit()
    except Exception as e:
        error_handle(e)

# About


def about():
    about = Toplevel()
    about.resizable(False, False)
    about.title("About FYFetcher")
    frame = LabelFrame(about, text=f"FYFetcher {version}")
    frame.pack(padx=5, pady=5)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")
    lbox = Text(frame, yscrollcommand=scrollbar.set, height=25, width=50)
    lbox.pack()
    lbox.insert(END, License)
    scrollbar.config(command=lbox.yview)


# Menubar
menubar = Menu(root)

file = Menu(menubar, tearoff=0)
# Add the File section
menubar.add_cascade(label='File', menu=file)
# Add the New Download section
file.add_command(label="New Download", command=new_download)
file.add_command(label="New YouTube Download", command=new_video)
file.add_separator()
# Add the Open Folder section
file.add_command(label="Open Folder", command=path)
file.add_separator()
# Add the Exit section
file.add_command(label="Exit", command=root.destroy)

edit = Menu(menubar, tearoff=0)
# Add the Edit section
menubar.add_cascade(label="Edit", menu=edit)
# Add the Clear Log section
edit.add_command(label="Clear Log", command=clear)

help_ = Menu(menubar, tearoff=0)
# Add the Help section
menubar.add_cascade(label="Help", menu=help_)
# Add the About section
help_.add_command(label="About FYFetcher", command=about)
# Add the Help section
help_.add_command(label="FYFetcher Help", command=help_link)
# Add the Update section
help_.add_command(label="Update FYFetcher", command=update)

# Set the menubar
root.config(menu=menubar)

# Create the scrollbar
scrollbar = Scrollbar(root)
# Create the log box
output = Text(root, height=20, width=55, state=DISABLED)
# Config the scrollbar working on the log box
scrollbar.config(command=output.yview)
output.config(yscrollcommand=scrollbar.set)

output.grid(column=0, row=0)
scrollbar.grid(row=0, column=1, sticky="ns")


root.mainloop()
