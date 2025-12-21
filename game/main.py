from pygame import mixer
import tkinter as tk
import os
from tkinter import filedialog

mixer.init()


def play_music():
    song = "music\joy.mp3"
    playlist.get(tk.ACTIVE)
    mixer.music.load(song)
    mixer.music.play()


def pause_music():
    mixer.music.pause()


def resume_music():
    mixer.music.unpause()


def stop_music():
    mixer.music.stop()


def load_music():
    directory = filedialog.askdirectory()
    if directory:
        os.chdir(directory)
        songs = os.listdir(directory)
        playlist.delete(0, tk.END)
        for song in songs:
            if song.endswith("joy.mp3"):
                playlist.insert(tk.END, song)


control_frame = tk.Frame(root, bg="#1e1e1e")
control_frame.pack()
tk.Button(control_frame, text="play", command=play_music, width=10, bg="green").grid(
    row=0, column=0, padx=5
)
tk.Button(control_frame, text="pause", command=pause_music, width=10, bg="orange").grid(
    row=0, column=1, padx=5
)
tk.Button(control_frame, text="resume", command=resume_music, width=10, bg="blue").grid(
    row=0, column=2, padx=5
)
tk.Button(control_frame, text="stop", command=stop_music, width=10, bg="red").grid(
    row=0, column=3, padx=5
)
tk.Button(
    control_frame, text="load music Folder", command=load_music, width=20, bg="#444"
).pack(pady=10)

root.mainloop()
