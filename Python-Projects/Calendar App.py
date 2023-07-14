# Calendar App

import tkinter as tk
from tkinter import messagebox
import calendar

def show_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())

    try:
        cal = calendar.monthcalendar(year, month)
        calendar_str = calendar.month_name[month] + " " + str(year) + "\n\n"
        calendar_str += "Mon Tue Wed Thu Fri Sat Sun\n"

        for week in cal:
            for day in week:
                if day == 0:
                    calendar_str += "    "
                else:
                    calendar_str += f"{day:2d}  "
            calendar_str += "\n"

        messagebox.showinfo("Calendar", calendar_str)
    except ValueError:
        messagebox.showerror("Error", "Invalid year or month!")

# Create the main window
window = tk.Tk()
window.title("Calendar App")

# Year input
year_label = tk.Label(window, text="Year:")
year_label.pack()

year_entry = tk.Entry(window)
year_entry.pack()

# Month input
month_label = tk.Label(window, text="Month:")
month_label.pack()

month_entry = tk.Entry(window)
month_entry.pack()

# Show calendar button
show_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_button.pack()

# Run the main loop
window.mainloop()
