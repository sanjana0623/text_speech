#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create tkinter main window
root = tk.Tk()
root.title("Text-to-Speech Application")

# Function to speak the entered text
def speak_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

# Function to save speech as audio file
def save_as_audio():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        filename = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")])
        if filename:
            engine.save_to_file(text, filename)
            engine.runAndWait()

# GUI Layout
text_label = tk.Label(root, text="Enter Text:")
text_label.pack(pady=10)

text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

language_label = tk.Label(root, text="Select Language:")
language_label.pack(pady=5)

# Example dropdown menu for language selection
languages = ['en', 'es', 'fr']  # Example languages
language_dropdown = ttk.Combobox(root, values=languages, width=10)
language_dropdown.pack()

voice_label = tk.Label(root, text="Select Voice:")
voice_label.pack(pady=5)

# Example dropdown menu for voice selection
voices = engine.getProperty('voices')
voice_names = [voice.name for voice in voices]
voice_dropdown = ttk.Combobox(root, values=voice_names, width=40)
voice_dropdown.pack()

# Example sliders for speech parameters
rate_label = tk.Label(root, text="Rate:")
rate_label.pack(pady=5)

rate_slider = tk.Scale(root, from_=50, to=300, orient=tk.HORIZONTAL)
rate_slider.pack()

# Example buttons for playback controls
play_button = tk.Button(root, text="Play", command=speak_text)
play_button.pack(pady=5)

save_button = tk.Button(root, text="Save Audio", command=save_as_audio)
save_button.pack(pady=5)

# Run the tkinter main loop
root.mainloop()


# Function to set TTS engine properties
def set_properties():
    selected_language = language_dropdown.get()
    selected_voice = voice_dropdown.get()

    engine.setProperty('rate', rate_slider.get())  # Speed percent (can go over 100)
    # engine.setProperty('volume', volume_slider.get())  # Volume 0-1
    # engine.setProperty('pitch', pitch_slider.get())  # Pitch (50-200)
    engine.setProperty('voice', selected_voice)
    engine.setProperty('language', selected_language)

