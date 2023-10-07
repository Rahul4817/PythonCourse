import tkinter as tk

root = tk.Tk()
root.title("Frame Example")

# Create a frame
frame = tk.Frame(root)
frame.pack()

# Add widgets to the frame
label = tk.Label(frame,bg="yellow",fg="blue",width=50,height=10,text="This is a label inside the frame")
label.pack(padx=20)

button = tk.Button(frame, text="Click Me")
button.pack()

root.mainloop()