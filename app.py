import tkinter
import customtkinter
from level import LevelCalculator
from data import projects

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

class LevelCalculatorApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('42 Level Calculator by z4ck')
        self.geometry('500x700')
        self.resizable(False, False)

        # Variables
        self.slevel_var = tkinter.DoubleVar(value=0.0)
        self.xp_var = tkinter.IntVar(value=0)
        self.score_var = tkinter.IntVar(value=100)
        self.switch_var = tkinter.StringVar(value='off')
        self.result_var = tkinter.DoubleVar()

        # Configure Grid
        self.grid_columnconfigure(0, weight=1)

        # Title Label
        title_label = customtkinter.CTkLabel(self, text='42 Level Calculator', font=('Arial', 24, 'bold'))
        title_label.grid(row=0, column=0, pady=(20, 10))

        # Current Level Frame
        level_frame = customtkinter.CTkFrame(self)
        level_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        level_label = customtkinter.CTkLabel(level_frame, text='Current Level:', font=('Arial', 17))
        level_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        level_entry = customtkinter.CTkEntry(level_frame, font=('Arial', 15), textvariable=self.slevel_var)
        level_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Project Selection Frame
        project_frame = customtkinter.CTkFrame(self)
        project_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        project_label = customtkinter.CTkLabel(project_frame, text='Select Project:', font=('Arial', 17))
        project_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.optionmenu_var = customtkinter.StringVar(value="Choose a project")
        project_optionmenu = customtkinter.CTkComboBox(project_frame, values=list(projects.keys()),
                                                       command=self.optionmenu_callback,
                                                       variable=self.optionmenu_var,
                                                       font=('Arial', 15))
        project_optionmenu.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Score Frame
        score_frame = customtkinter.CTkFrame(self)
        score_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        score_label = customtkinter.CTkLabel(score_frame, text='Project Score:', font=('Arial', 17))
        score_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        score_entry = customtkinter.CTkEntry(score_frame, font=('Arial', 15), textvariable=self.score_var)
        score_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Coalition Bonus Switch
        bonus_switch = customtkinter.CTkSwitch(self, text='Include Coalition Bonus',
                                               font=('Arial', 15), variable=self.switch_var,
                                               onvalue='on', offvalue='off', command=self.calculate)
        bonus_switch.grid(row=4, column=0, pady=20)

        # Calculate Button
        calculate_button = customtkinter.CTkButton(self, text='Calculate', font=('Arial', 17, 'bold'),
                                                   command=self.calculate)
        calculate_button.grid(row=5, column=0, padx=100, pady=10, sticky="ew")

        # Result Frame
        result_frame = customtkinter.CTkFrame(self)
        result_frame.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

        self.result_label = customtkinter.CTkLabel(result_frame, text='', font=('Arial', 20))
        self.result_label.pack(pady=10)

        # Update Button
        self.update_button = customtkinter.CTkButton(self, text='', font=('Arial', 15), command=self.update_level)
        self.update_button.grid(row=7, column=0, pady=10)
        self.update_button.grid_remove()  # Initially hidden

        # Footer Label
        footer_label = customtkinter.CTkLabel(self, text='Made by z4ck\n github @callmezaki', font=('Arial', 12))
        footer_label.grid(row=8, column=0, pady=(20, 10))

    def optionmenu_callback(self, choice):
        self.xp_var.set(projects[choice])

    def calculate(self):
        try:
            start_level = float(self.slevel_var.get() or 0)  # Fallback to 0 if empty
            planned_xp = int(self.xp_var.get() or 0)  # Fallback to 0 if empty
            score = int(self.score_var.get() or 0)  # Fallback to 0 if empty
            switch_value = self.switch_var.get()

            if start_level < 0 or planned_xp < 0 or score < 0:
                raise ValueError("Values must be non-negative")

            res = LevelCalculator(start_level, planned_xp, score, switch_value)
            res = round(res, 2)
            self.result_var.set(res)
            self.result_label.configure(text=f"Projected End Level: {res}")
            self.update_button.configure(text=f'Update Current Level to {res}')
            self.update_button.grid()  # Show the update button
        except ValueError as e:
            self.result_label.configure(text=f"Error: {str(e)}")
            self.update_button.grid_remove()  # Hide the update button on error

    def update_level(self):
        self.slevel_var.set(self.result_var.get())
        self.result_label.configure(text='Current level updated.')
        self.update_button.grid_remove()  # Hide the update button after updating

if __name__ == "__main__":
    app = LevelCalculatorApp()
    app.mainloop()
