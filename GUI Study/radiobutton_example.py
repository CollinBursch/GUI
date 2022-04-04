import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):    
        self.main_window = tkinter.Tk()
       
        self.radio_button_options_frame = tkinter.Frame(self.main_window)

        # Pizza size buttons
        self.radio_button_options_var = tkinter.IntVar()
        self.radio_button_options_var.set(0)

        self.option1 = tkinter.Radiobutton(
            self.radio_button_options_frame, text="Collin", variable=self.radio_button_options_var, value=1
        )
        self.option2 = tkinter.Radiobutton(
            self.radio_button_options_frame, text="Carson", variable=self.radio_button_options_var, value=2
        )
        self.option3 = tkinter.Radiobutton(
            self.radio_button_options_frame, text="Des", variable=self.radio_button_options_var, value=3
        )
        self.option4 = tkinter.Radiobutton(
            self.radio_button_options_frame, text="Dylan", variable=self.radio_button_options_var, value=4
        )

        
        self.option1.pack(side='left')
        self.option2.pack(side='left')
        self.option3.pack(side='left')
        self.option4.pack(side='left')

        self.radio_button_options_frame.pack()

        tkinter.mainloop()

radiobutton_example = MyGUI()