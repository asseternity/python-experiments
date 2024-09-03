import tkinter as tk

window = tk.Tk()
window.title("Hello, World!")

def handle_any_button_press(event):
    window.destroy()

button = tk.Button(text="Close the app")
button.bind("<Button-1>", handle_any_button_press)
button.pack()

window.mainloop()