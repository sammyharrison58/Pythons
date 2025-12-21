import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pygame import mixer

# Supported audio file extensions
AUDIO_EXTS = {".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"}

# Initialize pygame mixer
try:
    mixer.init()
except Exception as e:
    print(f"Warning: mixer.init() failed: {e}")

# Create Tk root
root = tk.Tk()
root.title("Simple Music Player")
root.geometry("600x380")
root.configure(bg="#1e1e1e")

# Track the current music directory
current_music_dir = None

# Layout: left for playlist, right for controls
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = tk.Frame(main_frame, bg="#1e1e1e")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(main_frame, bg="#1e1e1e")
right_frame.pack(side="right", fill="y")

# Playlist with scrollbar
scrollbar = tk.Scrollbar(left_frame, orient="vertical")
playlist = tk.Listbox(
    left_frame,
    bg="#111",
    fg="#ddd",
    selectbackground="#444",
    activestyle="dotbox",
    height=18,
)
playlist.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
playlist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=playlist.yview)


def get_selected_song_path() -> str | None:
    """Return absolute path of selected song or None."""
    sel = playlist.curselection()
    if not sel:
        return None
    filename = playlist.get(sel[0])
    if current_music_dir is None:
        return None
    return os.path.join(current_music_dir, filename)


def play_music():
    """Play selected song; default to first if none selected."""
    if playlist.size() == 0:
        messagebox.showinfo("Play", "No songs loaded. Load a music folder first.")
        return

    if not playlist.curselection():
        playlist.selection_set(0)
        playlist.activate(0)

    song_path = get_selected_song_path()
    if not song_path:
        messagebox.showinfo("Play", "Please select a song to play.")
        return

    try:
        mixer.music.load(song_path)
        mixer.music.play()
    except Exception as e:
        messagebox.showerror(
            "Error", f"Failed to play '{os.path.basename(song_path)}'\n{e}"
        )


def pause_music():
    try:
        mixer.music.pause()
    except Exception:
        pass


def resume_music():
    try:
        mixer.music.unpause()
    except Exception:
        pass


def stop_music():
    try:
        mixer.music.stop()
    except Exception:
        pass


def load_music():
    """Ask for a directory and populate the playlist with audio files."""
    global current_music_dir
    directory = filedialog.askdirectory()
    if not directory:
        return

    try:
        items = sorted(os.listdir(directory))
        songs = [
            f
            for f in items
            if os.path.isfile(os.path.join(directory, f))
            and os.path.splitext(f)[1].lower() in AUDIO_EXTS
        ]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read directory:\n{e}")
        return

    playlist.delete(0, tk.END)
    if not songs:
        current_music_dir = None
        messagebox.showinfo(
            "No audio", "No supported audio files found in the selected folder."
        )
        return

    for s in songs:
        playlist.insert(tk.END, s)

    current_music_dir = directory


# Double click to play
playlist.bind("<Double-1>", lambda e: play_music())

# Controls (only use grid in right_frame)
tk.Label(
    right_frame, text="Controls", bg="#1e1e1e", fg="#ddd", font=("Segoe UI", 11, "bold")
).grid(row=0, column=0, columnspan=2, pady=(0, 10))

btn_kwargs = dict(width=14)
pad = dict(padx=6, pady=6)

tk.Button(
    right_frame,
    text="Load Folder",
    command=load_music,
    bg="#444",
    fg="#eee",
    **btn_kwargs,
).grid(row=1, column=0, columnspan=2, sticky="ew", **pad)
tk.Button(
    right_frame, text="Play", command=play_music, bg="green", fg="#fff", **btn_kwargs
).grid(row=2, column=0, sticky="ew", **pad)
tk.Button(
    right_frame, text="Pause", command=pause_music, bg="orange", fg="#000", **btn_kwargs
).grid(row=2, column=1, sticky="ew", **pad)
tk.Button(
    right_frame, text="Resume", command=resume_music, bg="blue", fg="#fff", **btn_kwargs
).grid(row=3, column=0, sticky="ew", **pad)
tk.Button(
    right_frame, text="Stop", command=stop_music, bg="red", fg="#fff", **btn_kwargs
).grid(row=3, column=1, sticky="ew", **pad)

root.mainloop()
