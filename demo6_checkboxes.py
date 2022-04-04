import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create three IntVar objects to use with the checkboxes

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # set the IntVar objects to 8
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.top_frame, text="Option 1", variable=self.cb_var1
        )
        self.cb2 = tkinter.Checkbutton(
            self.top_frame, text="Option 2", variable=self.cb_var2
        )
        self.cb3 = tkinter.Checkbutton(
            self.top_frame, text="Option 3", variable=self.cb_var3
        )

        tkinter.mainloop()

    def do_something(self):

        self.message = "You have selected: \n"

        if self.cb_var1.get() == 1:
            self.message == "1\n"
        if self.cb_var2.get() == 1:
            self.message == "2\n"
        if self.cb_var3.get() == 1:
            self.message == "3\n"

        tkinter.messagebox.showinfo("response", "Thanks for clickign the button")

        tkinter.mainloop()


my_gui = MyGUI()

print("moving on......")
