import tkinter
import tkinter.messagebox


class KiloConverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(
            self.top_frame, text="Enter a distance in Kilometers: "
        )
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.descr_label = tkinter.Label(self.mid_frame, text="Converted to miles:")

        self.miles_var = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.miles_var)

        self.calcbutton = tkinter.Button(
            self.main_window, text="Convert!", command=self.do_something
        )

        # have to pack the frames too!
        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.calcbutton.pack(side="left")
        self.quit_button.pack(side="right")

        self.top_frame.pack(text="top")
        self.bottom_frame.pack(text="bottom")

        tkinter.mainloop()

    def do_something(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo * 0.6214), 2)

        tkinter.messagebox.showinfo(
            "Results", str(kilo) + " kilometers is equal to " + str(miles) + "miles"
        )

        tkinter.mainloop()


my_gui = MyGUI()

print("moving on......")
