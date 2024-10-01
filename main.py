import tkinter as tk

def key_press(event):
    # Update the label with the pressed key
    label.config(text=f"Você pressionou: {event.char}")

# Create the main window
root = tk.Tk()
root.title("Python3")

# Create a label to display the key pressed
label = tk.Label(root, text="Aperte qualquer tecla", font=("Segoe UI", 24))
label.pack(pady=50)

# Bind the key press event to the key_press function
root.bind("<Key>", key_press)

# Start the main loop
root.mainloop()
