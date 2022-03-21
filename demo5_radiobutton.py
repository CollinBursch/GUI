import tkinter
import tkinter.messagebox


class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        # set the InVar object to 1
        self.radio_var.set(10)

        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text="Option 1", variable=self.radio_var, value=1
        )

        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text="Option 2", variable=self.radio_var, value=2
        )

        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text="Option 3", variable=self.radio_var, value=3
        )

        # pack

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # pack
        # have to pack the frames too!
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        
        self.ok_button = tkinter.Button(
            self.bottom_frame, text="OK", command=self.show_choice
        )

        self.reset_button = tkinter.Button(
            self.bottom_frame, text="Reset", command=self.rb1.select
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.ok_button.pack(side="left")
        self.reset_button.pack(side="left")
        self.quit_button.pack(side="top")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo(
            "Selection", "You have selection option" + str(self.radio_var.get())
        )

kilo_conv = KiloConverterGUI()

print("moving on......")
