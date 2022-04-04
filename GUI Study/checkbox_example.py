 # Create topping check boxes
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):    
        self.main_window = tkinter.Tk()

        self.check_boxes_frame = tkinter.Frame(self.main_window)

        self.option1 = tkinter.IntVar()
        self.option2 = tkinter.IntVar()
        self.option3 = tkinter.IntVar()
        self.option4 = tkinter.IntVar()

        # set the IntVar objects to 0
        self.option1.set(0)
        self.option2.set(0)
        self.option3.set(0)
        self.option4.set(0)
        
        self.option1_cb = tkinter.Checkbutton(
            self.check_boxes_frame, text="Option 1", variable=self.option1
        )
        self.option2_cb = tkinter.Checkbutton(
            self.check_boxes_frame, text="Option 2", variable=self.option2
        )
        self.option3_cb = tkinter.Checkbutton(
            self.check_boxes_frame, text="Option 3", variable=self.option3
        )
        self.option4_cb = tkinter.Checkbutton(
            self.check_boxes_frame, text="Option 4", variable=self.option4
        )


        self.option1_cb.pack(side="left")
        self.option2_cb.pack(side="left")
        self.option3_cb.pack(side="left")
        self.option4_cb.pack(side="left")
 
        self.check_boxes_frame.pack()

        tkinter.mainloop()

check_boxes_example = MyGUI()
