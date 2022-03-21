import tkinter
import tkinter.messagebox

'''
Design a creative UI using Python's tkinter module to calculate the total cost of a pizza. The UI should have (at least) each widget that was covered in class:

Frames
Labels
input box
buttons
radio buttons
check boxes
You can use check boxes for for selecting toppings (each with a different cost), radio buttons for the type of crust selected (each with a different cost), buttons for calculation and quit. The input box can be used to record the name of the person placing the order. Use a message box to display the total cost of the pizza along with the name of the person placing the order.

Make sure your design is well laid out and intuitive to the user. Take account of spacing and packing so that everything is properly aligned and professional looking. Be creative with font, color, size, etc.
'''

class ScoreAverager:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.top_1_frame = tkinter.Frame(self.top_frame)
        self.top_2_frame = tkinter.Frame(self.top_frame)
        self.top_3_frame = tkinter.Frame(self.top_frame)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label1 = tkinter.Label(
            self.top_1_frame, text="Enter the score for test 1: "
        )
        self.test1_entry = tkinter.Entry(self.top_1_frame, width=10)

        self.prompt_label2 = tkinter.Label(
            self.top_2_frame, text="Enter the score for test 2: "
        )
        self.test2_entry = tkinter.Entry(self.top_2_frame, width=10)

        self.prompt_label3 = tkinter.Label(
            self.top_3_frame, text="Enter the score for test 3: "
        )
        self.test3_entry = tkinter.Entry(self.top_3_frame, width=10)

        self.prompt_label1.pack(side="left")
        self.test1_entry.pack(side="left")

        self.prompt_label2.pack(side="left")
        self.test2_entry.pack(side="left")

        self.prompt_label3.pack(side="left")
        self.test3_entry.pack(side="left")

        self.top_1_frame.pack(side="top")
        self.top_2_frame.pack(side="top")
        self.top_3_frame.pack(side="top")


        self.avg_label = tkinter.Label(self.mid_frame, text="Average: ")

        self.avg_var = tkinter.StringVar()
        self.avg_var.set('None')

        self.avg = tkinter.Label(self.mid_frame, textvariable=self.avg_var)

        self.avg_label.pack(side="left")
        self.avg.pack(side="left")

        self.calcbutton = tkinter.Button(
            self.bottom_frame, text="Average", command=self.calc_avg
        )

        # # have to pack the frames too!
        self.quit_button = tkinter.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy
        )

        self.calcbutton.pack(side="left")
        self.quit_button.pack(side="right")

        self.top_frame.pack(side="top")  # not sure if it is side or text
        self.mid_frame.pack(side="top")
        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def calc_avg(self):
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())

        avg_score = ((test1 + test2 + test3)/ 3)
        self.avg_var.set(str(avg_score))

        tkinter.mainloop()


score_avger = ScoreAverager()

print("moving on......")
