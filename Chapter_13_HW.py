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

class CollinsPizza:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.shop_info_frame = tkinter.Frame(self.main_window)
        self.order_name_frame = tkinter.Frame(self.main_window)
        self.pizza_size_frame = tkinter.Frame(self.main_window)
        self.crust_type_frame = tkinter.Frame(self.main_window)
        self.sauce_type_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        self.command_buttons_frame = tkinter.Frame(self.main_window)

        # Shop info frame
        self.shop_name = tkinter.Label(
            self.shop_info_frame, text= "Collin's Pizza Shop", font= ("Helvetica", 20, "bold underline"), fg='red'
        )        
        self.shop_name.pack(side="top")
        self.shop_info_frame.pack(side="top")

        # Order name frame
        self.prompt_name_label = tkinter.Label(
            self.order_name_frame, text="Name for Order: ", font= ("Helvetica", 10, "bold")
        )
        self.name_entry = tkinter.Entry(self.order_name_frame, width=18)

        self.prompt_name_label.pack(side="left")
        self.name_entry.pack(side="left")
        self.order_name_frame.pack(side="top")

        # Pizza size frame 
        self.pizza_size = tkinter.Label(
            self.pizza_size_frame, text ="Pizza Size: ", font= ("Helvetica", 10, "bold")
        )
        # Pizza size buttons
        self.pizza_size_var = tkinter.IntVar()
        self.pizza_size_var.set(0)
        self.small = tkinter.Radiobutton(
            self.pizza_size_frame, text="Small ($10)", variable=self.pizza_size_var, value=10
        )
        self.medium = tkinter.Radiobutton(
            self.pizza_size_frame, text="Medium ($14)", variable=self.pizza_size_var, value=14
        )
        self.large = tkinter.Radiobutton(
            self.pizza_size_frame, text="Large ($18)", variable=self.pizza_size_var, value=18
        )
        self.extra_large = tkinter.Radiobutton(
            self.pizza_size_frame, text="Extra Large ($22)", variable=self.pizza_size_var, value=22
        )

        self.pizza_size.pack()

        self.small.pack(side='left')
        self.medium.pack(side='left')
        self.large.pack(side='left')
        self.extra_large.pack(side='left')

        self.pizza_size_frame.pack()

        # Type of crust size frame 
        self.crust = tkinter.Label(
            self.crust_type_frame, text ="Type of Crust: ", font= ("Helvetica", 10, "bold")
        )
        # Type of crust buttons
        self.crust_var = tkinter.IntVar()
        self.crust_var.set(0)
        self.plain_thin = tkinter.Radiobutton(
            self.crust_type_frame, text="Plain Thin ($0)", variable=self.crust_var, value=0
        )
        self.plain_thick = tkinter.Radiobutton(
            self.crust_type_frame, text="Plain Thick ($1)", variable=self.crust_var, value=1
        )
        self.cheese = tkinter.Radiobutton(
            self.crust_type_frame, text="Cheese ($4)", variable=self.crust_var, value=4
        )
        self.garlic = tkinter.Radiobutton(
            self.crust_type_frame, text="Garlic ($3)", variable=self.crust_var, value=3
        )
        self.stuffed = tkinter.Radiobutton(
            self.crust_type_frame, text="Stuffed ($5)", variable=self.crust_var, value=5
        )

        self.crust.pack()

        self.plain_thin.pack(side='left')
        self.plain_thick.pack(side='left')
        self.cheese.pack(side='left')
        self.garlic.pack(side='left')
        self.stuffed.pack(side='left')

        self.crust_type_frame.pack()

        # Sauce Type frame 
        self.sauce = tkinter.Label(
            self.sauce_type_frame, text ="Type of Sauce: ", font= ("Helvetica", 10, "bold")
        )
        # Sauce Type buttons
        self.sauce_var = tkinter.IntVar()
        self.sauce_var.set(0)
        self.white = tkinter.Radiobutton(
            self.sauce_type_frame, text="White ($2)", variable=self.sauce_var, value=2
        )
        self.marinara = tkinter.Radiobutton(
            self.sauce_type_frame, text="Marinara ($0)", variable=self.sauce_var, value=0
        )
        self.pesto = tkinter.Radiobutton(
            self.sauce_type_frame, text="Pesto ($1)", variable=self.sauce_var, value=1
        )
        self.buffalo_ranch = tkinter.Radiobutton(
            self.sauce_type_frame, text="Buffalo Ranch ($3)", variable=self.sauce_var, value=3
        )

        self.sauce.pack()

        self.white.pack(side='left')
        self.marinara.pack(side='left')
        self.pesto.pack(side='left')
        self.buffalo_ranch.pack(side='left')

        self.sauce_type_frame.pack()

        # Toppings frame
        self.toppings_label = tkinter.Label(
            self.toppings_frame, text ="Select Toppings: ", font= ("Helvetica", 10, "bold")
        )
        # Create topping check boxes
        self.cheese = tkinter.IntVar()
        self.sausage = tkinter.IntVar()
        self.pepperoni = tkinter.IntVar()
        self.bacon = tkinter.IntVar()
        self.olives = tkinter.IntVar()
        self.onions = tkinter.IntVar()
        self.mushrooms = tkinter.IntVar()
        self.garlic = tkinter.IntVar()

        # set the IntVar objects to 8
        self.cheese.set(0)
        self.sausage.set(0)
        self.pepperoni.set(0)
        self.bacon.set(0)
        self.olives.set(0)
        self.onions.set(0)
        self.mushrooms.set(0)
        self.garlic.set(0)
        
        self.cheese_cb = tkinter.Checkbutton(
            self.toppings_frame, text="Cheese ($0)", variable=self.cheese
        )
        self.sausage_cb = tkinter.Checkbutton(
            self.toppings_frame, text="Sausage ($2)", variable=self.sausage
        )
        self.pepperoni_cb = tkinter.Checkbutton(
            self.toppings_frame, text="Pepperoni ($2)", variable=self.pepperoni
        )
        self.bacon_cb = tkinter.Checkbutton(
            self.toppings_frame, text="Bacon ($3)", variable=self.bacon
        )
        self.olives_cb = tkinter.Checkbutton(
            self.toppings_frame, text="Olives ($1)", variable=self.olives
        )
        self.onions_cb = tkinter.Checkbutton(
            self.toppings_frame, text="Onions ($1)", variable=self.onions
        )
        self.mushrooms_cb = tkinter.Checkbutton(
            self.toppings_frame, text="Mushrooms ($1)", variable=self.mushrooms
        )
        self.garlic_cb = tkinter.Checkbutton(
            self.toppings_frame, text="Garlic ($1)", variable=self.garlic
        )

        self.toppings_label.pack()
        self.cheese_cb.pack(side="left")
        self.sausage_cb.pack(side="left")
        self.pepperoni_cb.pack(side="left")
        self.bacon_cb.pack(side="left")
        self.olives_cb.pack(side="left")
        self.onions_cb.pack(side="left")
        self.mushrooms_cb.pack(side="left")
        self.garlic_cb.pack(side="left")

        self.toppings_frame.pack()

        # Command buttons frame
        self.completeOrder = tkinter.Button(
            self.command_buttons_frame, text="Complete Order", command=self.complete_order, font= ("Helvetica", 10, "bold")
        )
        self.quit_button = tkinter.Button(
            self.command_buttons_frame, text="Quit", command=self.main_window.destroy, font= ("Helvetica", 10, "bold")
        )
        self.completeOrder.pack(side="left")
        self.quit_button.pack(side="right")
        self.command_buttons_frame.pack()

        tkinter.mainloop()

    def complete_order(self):
        total = (self.pizza_size_var.get() + self.crust_var.get() + self.sauce_var.get() + 
                 self.cheese.get() * 0 + self.sausage.get() * 2 + self.pepperoni.get() * 2 +
                 + self.bacon.get() * 3 + self.olives.get() * 1 + self.onions.get() * 1 
                 + self.mushrooms.get() * 1+ self.garlic.get() * 1
                )

        tkinter.messagebox.showinfo(
            "Order Summary", "Name: " + self.name_entry.get() + "\nTotal: $" + str(total)
        )

        tkinter.mainloop()



Collins_Pizza = CollinsPizza()

print("moving on......")
