import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):    
        self.main_window = tkinter.Tk()

        self.command_button_frame = tkinter.Frame(self.main_window)
        
        self.continue_button = tkinter.Button(
                self.command_button_frame, text="Continue", command=self.continue_function
            )
        self.quit_button = tkinter.Button(
                self.command_button_frame, text="Quit", command=self.main_window.destroy
            )
                
        self.continue_button.pack(side="left")
        self.quit_button.pack(side="right")
        self.command_button_frame.pack()

        tkinter.mainloop()

    def continue_function(self):

        tkinter.messagebox.showinfo(
            "Cahson", "Alt string 1"
        )

        tkinter.mainloop()

messagebox_example = MyGUI()