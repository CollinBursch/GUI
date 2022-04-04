import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):   
        self.main_window = tkinter.Tk()

        self.labels_frame1 = tkinter.Frame(self.main_window)
        self.labels_frame2 = tkinter.Frame(self.main_window)


        self.label1 = tkinter.Label(
            self.labels_frame1, text="First Name: ", font= ("Helvetica", 10, "bold")
        )

        self.label2 = tkinter.Label(
            self.labels_frame1, text="Middle Name: ", font= ("Helvetica", 10, "bold")
        )
        
        self.label3 = tkinter.Label(
            self.labels_frame2, text="Last Name: ", font= ("Helvetica", 10, "bold")
        )

        self.name_entry1 = tkinter.Entry(self.labels_frame1, width=18)
        self.name_entry2 = tkinter.Entry(self.labels_frame1, width=18)
        self.name_entry3 = tkinter.Entry(self.labels_frame2, width=18)

        self.label1.pack(side="left")
        self.name_entry1.pack(side="left")

        self.label2.pack(side="left")
        self.name_entry2.pack(side="left")

        self.label3.pack(side="left")
        self.name_entry3.pack(side="left")

        self.labels_frame1.pack()
        self.labels_frame2.pack()
        
        tkinter.mainloop()

labels_example = MyGUI()
            
