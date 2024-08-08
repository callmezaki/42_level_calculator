import tkinter
import customtkinter
from level import LevelCalculator
from data import projects

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('400x600')
app.title('42 Level Calculator by z4ck')

def calculate():
    try:
        start_level = float(slevel_var.get())
        planned_xp = int(xp_var.get())
        score = int(score_var.get())
        switch_value = switch_var.get()
        if start_level < 0 or planned_xp < 0:
            raise ValueError("Values must be non-negative")
        res = LevelCalculator(start_level, planned_xp, score,switch_value)
        res = round(res, 2)
        result_label.configure(text=f"End Level: {res}")
    except ValueError as e:
        result_label.configure(text=f"Error: {str(e)}")

# Current Level Label and Entry
current_level_label = customtkinter.CTkLabel(app, text='Current Level:', font=('Arial', 17))
current_level_label.pack(pady=10)

slevel_var = tkinter.DoubleVar()
current_level_entry = customtkinter.CTkEntry(app, font=('Arial', 12), textvariable=slevel_var)
current_level_entry.pack(pady=10, padx=10)

# Project XP Label and Entry
xp_label = customtkinter.CTkLabel(app, text='Project XP:', font=('Arial', 17))
xp_label.pack(pady=10)

xp_var = tkinter.IntVar()
xp_entry = customtkinter.CTkEntry(app, font=('Arial', 12), textvariable=xp_var)
xp_entry.pack(pady=10, padx=10)

score_label = customtkinter.CTkLabel(app, text='Project score:', font=('Arial', 17))
score_label.pack(pady=10)

score_var = tkinter.IntVar()
score_var.set(100)
score_entry = customtkinter.CTkEntry(app, font=('Arial', 12), textvariable=score_var)
score_entry.pack(pady=10, padx=10)

# switch On Off

switch_var = tkinter.StringVar(value='off')
switch = customtkinter.CTkSwitch(app, text='Coalition Bonus', font=('Arial', 15), variable=switch_var, onvalue='on', offvalue='off', command=calculate)
switch.pack(pady=20)

# Calculate Button
calculate_button = customtkinter.CTkButton(app, text='Calculate', font=('Arial', 15), command=calculate)
calculate_button.pack(pady=20)



# Result Label
result_label = customtkinter.CTkLabel(app, text='', font=('Arial', 17))
result_label.pack(pady=10)

app.mainloop()
