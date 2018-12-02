import tkinter as tk


# Some helper functions
def set_value():
    # get the value from input
    print(first_input.get())


# make an instance of tkinter
root = tk.Tk()
# Set app name
root.title('My First Desktop App')

# create frame
first_frame = tk.Frame(root)

# mount an frame
first_frame.pack()

second_frame = tk.Frame(root)
# side can be top left bottom right default top
second_frame.pack(side="bottom")

# create an label
first_input_label = tk.Label(first_frame, text="Input something")
first_input_label.pack()

# create an input
first_input = tk.Entry(first_frame)
first_input.pack()
first_input.focus_set()

# create an button
first_button = tk.Button(second_frame, text="Click me", fg="red", bg="blue", command=set_value)
first_button.pack()

close_button = tk.Button(second_frame, text="QUIT", fg="red", command=root.destroy)
close_button.pack()


# main loop
root.mainloop()



