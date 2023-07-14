# Stopwatch  

import tkinter as tk
from datetime import datetime

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = datetime.now()
            self.is_running = True

    def stop(self):
        if self.is_running:
            self.elapsed_time = datetime.now() - self.start_time
            self.is_running = False

    def reset(self):
        self.start_time = None
        self.is_running = False

def update_time():
    if stopwatch.is_running:
        elapsed_time = datetime.now() - stopwatch.start_time
        time_label.config(text=str(elapsed_time))
    else:
        time_label.config(text="00:00:00.000")
    window.after(10, update_time)

def start_stopwatch():
    stopwatch.start()

def stop_stopwatch():
    stopwatch.stop()

def reset_stopwatch():
    stopwatch.reset()

# Create the main window
window = tk.Tk()
window.title("Stopwatch")

# Create the stopwatch instance
stopwatch = Stopwatch()

# Create the time label
time_label = tk.Label(window, text="00:00:00.000", font=("Arial", 24))
time_label.pack(pady=20)

# Create the buttons
start_button = tk.Button(window, text="Start", command=start_stopwatch)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(window, text="Stop", command=stop_stopwatch)
stop_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(window, text="Reset", command=reset_stopwatch)
reset_button.pack(side=tk.LEFT, padx=10)

# Run the update_time loop
update_time()

# Run the main loop
window.mainloop()
