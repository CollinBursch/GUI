import tkinter
import tkinter.messagebox


class KiloConverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label1 = tkinter.Label(
            self.top_frame, text="Enter the score for test 1: "
        )
        self.test1_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label2 = tkinter.Label(
            self.mid_frame, text="Enter the score for test 2: "
        )
        self.test2_entry = tkinter.Entry(self.mid_frame, width=10)

        self.prompt_label3 = tkinter.Label(
            self.bottom_frame, text="Enter the score for test 3: "
        )
        self.test3_entry = tkinter.Entry(self.bottom_frame, width=10)

        self.prompt_label1.pack(side="left")
        self.test1_entry.pack(side="left")

        self.prompt_label2.pack(side="left")
        self.test2_entry.pack(side="left")

        self.prompt_label3.pack(side="left")
        self.test3_entry.pack(side="left")

        self.descr_label = tkinter.Label(self.mid_frame, text="Average of test scores")

        self.miles_var = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.miles_var)

        self.calcbutton = tkinter.Button(
            self.main_window, text="Average", command=self.do_something
        )

        # have to pack the frames too!
        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.calcbutton.pack(side="left")
        self.quit_button.pack(side="right")

        self.top_frame.pack(side="top")  # not sure if it is side or text
        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def do_something(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo * 0.6214), 2)

        tkinter.messagebox.showinfo(
            "Results", str(kilo) + " kilometers is equal to " + str(miles) + "miles"
        )

        tkinter.mainloop()


kilo_conv = KiloConverter()

print("moving on......")
